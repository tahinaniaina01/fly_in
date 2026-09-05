#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   drone_renderer.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/01 12:25:02 by trakotos            #+#    #+#            #
#   Updated: 2026/09/05 00:00:00 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from utils import Point
from typing import Any
from pygame import Surface, transform, image, error as PygameError
from .camera import Camera
from utils.utils import DRONE_SIZE
from time import time
from random import randint
import os


class DroneRenderer:
    # Chemin vers la feuille de sprites (à adapter à votre arborescence assets/)
    SPRITESHEET_PATH = os.path.join("assets", "birds.png")

    # Grille de la feuille de sprites : 7 frames d'animation x 4 couleurs d'oiseau
    FRAME_COLS = 8
    FRAME_ROWS = 4

    # Durée d'une frame d'animation en vol (secondes) -> vitesse du battement d'ailes
    ANIM_FRAME_DURATION = 0.07

    # Index de la frame "posée" (ailes fermées) dans chaque ligne d'animation
    LANDED_FRAME = 0

    # Cache partagé entre toutes les instances : on ne découpe la feuille qu'une fois
    _frames_cache: list[list[Surface]] | None = None

    def __init__(
        self,
        initial_pos: Point = Point(0, 0),
        path: list[Point] = [],
        color: Any = (40, 40, 40), size: int = DRONE_SIZE
    ) -> None:
        self.step = 0
        self.coord: Point = initial_pos
        self.size: int = size
        self.color = color
        self.center: Point = self.coord + (size // 2)
        self.is_moving = False
        self._move_start = self.coord
        self._move_end: Point = self.coord
        self._start_time = 0.0
        self._move_duration = 0.5
        self.path: list[Point] = path

        # --- Sélection aléatoire de l'oiseau et état d'animation ---
        # NB : on NE charge PAS la feuille de sprites ici. convert_alpha()
        # exige que pygame.display.set_mode() ait déjà été appelé, ce qui
        # n'est pas garanti au moment de la construction du drone.
        # Le chargement se fait paresseusement, au premier appel de render().
        self.bird_type: int = randint(0, self.FRAME_ROWS - 1)
        self.frame_index: int = self.LANDED_FRAME
        self._anim_timer: float = time()

        # Surface de repli si la feuille de sprites est introuvable
        # ou si le display n'est vraiment pas prêt
        self._fallback_surface = Surface((self.size, self.size), flags=0)
        self._fallback_surface.fill(self.color)

        print(path)

    # ------------------------------------------------------------------ #
    # Chargement / découpage de la feuille de sprites (lazy, une seule fois)
    # ------------------------------------------------------------------ #
    @classmethod
    def _get_bird_frames(cls) -> list[list[Surface]]:
        if cls._frames_cache is not None:
            return cls._frames_cache

        sheet = image.load(cls.SPRITESHEET_PATH).convert_alpha()
        sheet_w, sheet_h = sheet.get_size()

        cell_w = sheet_w / cls.FRAME_COLS
        cell_h = sheet_h / cls.FRAME_ROWS

        frames: list[list[Surface]] = []
        for row in range(cls.FRAME_ROWS):
            row_frames: list[Surface] = []
            for col in range(cls.FRAME_COLS):
                # Bornes arrondies pour éviter toute dérive d'arrondi cumulée
                x0 = round(col * cell_w)
                x1 = round((col + 1) * cell_w)
                y0 = round(row * cell_h)
                y1 = round((row + 1) * cell_h)
                frame = Surface((x1 - x0, y1 - y0), flags=0).convert_alpha()
                frame.fill((0, 0, 0, 0))
                frame.blit(sheet, (0, 0), area=(x0, y0, x1 - x0, y1 - y0))
                row_frames.append(frame)
            frames.append(row_frames)

        cls._frames_cache = frames
        return frames

    def _current_surface(self) -> Surface:
        try:
            frames = self._get_bird_frames()
        except (PygameError, FileNotFoundError):
            # Display pas encore prêt ou fichier introuvable -> repli
            return self._fallback_surface

        if not frames:
            return self._fallback_surface

        return frames[self.bird_type][self.frame_index]

    # ------------------------------------------------------------------ #
    # Déplacement (inchangé)
    # ------------------------------------------------------------------ #
    def move(self, dir: int = 1) -> bool:
        if self.is_moving and dir != 0:
            return False

        if self.step < len(self.path) - 1 and dir == 1:
            self.step += 1
        elif self.step > 0 and dir == -1:
            self.step -= 1
        elif dir == 0:
            self.step = 0
        self._move_start = self.coord
        self._move_end = self.path[self.step]
        self._start_time = time()
        self.is_moving = True

        return True

    def update(self) -> None:
        self._update_animation()

        if not self.is_moving:
            return

        elapsed = time() - self._start_time
        t = min((elapsed / self._move_duration), 1.0)

        self.coord = self._move_start + (self._move_end - self._move_start) * t

        if t >= 1.0:
            self.coord = self._move_end
            self.is_moving = False

    # ------------------------------------------------------------------ #
    # Animation : vol = boucle continue sur les 7 frames, posé = frame figée
    # ------------------------------------------------------------------ #
    def _update_animation(self) -> None:
        now = time()

        if not self.is_moving:
            # Posé : ailes fermées, on fige l'animation
            self.frame_index = self.LANDED_FRAME
            self._anim_timer = now
            return

        elapsed = now - self._anim_timer
        if elapsed >= self.ANIM_FRAME_DURATION:
            # On avance d'autant de frames que le temps écoulé le permet,
            # basé sur le temps réel (et pas sur le framerate) -> animation fluide
            steps = int(elapsed // self.ANIM_FRAME_DURATION)
            self.frame_index = (self.frame_index + steps) % self.FRAME_COLS
            self._anim_timer += steps * self.ANIM_FRAME_DURATION

    # ------------------------------------------------------------------ #
    # Rendu
    # ------------------------------------------------------------------ #
    def render(self, screen: Surface, camera: Camera) -> None:
        # IMPORTANT : on part toujours de la frame source d'origine pour le scale,
        # jamais d'une surface déjà mise à l'échelle (sinon effet boule de neige).
        source = self._current_surface()
        src_w, src_h = source.get_size()
        scaled = transform.scale(
            source,
            (int(src_w * camera.zoom), int(src_h * camera.zoom))
        )

        c = (self.coord - Point(camera.x, camera.y)) * camera.zoom
        self.center = c + ((self.size * camera.zoom) // 2)

        # Toutes les cellules ont la même taille -> pas de "saut" visuel
        # d'une frame à l'autre, même si l'envergure des ailes change.
        screen.blit(scaled, (c.x, c.y))

        self.update()
