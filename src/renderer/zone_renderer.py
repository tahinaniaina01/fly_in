#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   zone_renderer.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 15:29:31 by trakotos            #+#    #+#            #
#   Updated: 2026/09/06 15:22:18 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from dataclasses import dataclass
from typing import Any
from pygame import Surface, font, image, transform, error as PygameError
from utils import ZONE_ORIGIN, Point, ZONE_DISTANCE, ZONE_SIZE
from .camera import Camera
from models import Zone
import os


class ZoneRenderer:
    IMAGE_PATH = os.path.join("assets", "zones.png")
    FRAME_COLS = 3
    FRAME_ROWS = 2
    _frame_cache: list[list[Surface]] | None = None

    def __init__(
        self, zone: Zone,
        color: Any = (255, 0, 0), size: int = ZONE_SIZE
    ) -> None:
        if not font.get_init():
            font.init()

        self.zone = zone
        self.coord: Point = Point(zone.x, zone.y) * ZONE_DISTANCE + ZONE_ORIGIN
        self.color: Any = color
        self.size: int = size
        self.center: Point = self.coord + (self.size // 2)
        self.surface = Surface((self.size, self.size))
        self.image_coord: tuple[int, int] = (0, 0)
        if zone.zone_type == "blocked":
            self.image_coord = (2, 1)
        elif zone.zone_type == "normal":
            self.image_coord = (0, 1)
        elif zone.zone_type == "priority":
            self.image_coord = (2, 0)
        elif zone.zone_type == "restricted":
            self.image_coord = (1, 1)
        if zone.is_start:
            self.image_coord = (0, 0)
        if zone.is_end:
            self.image_coord = (1, 0)
        self.surface.fill(self.color)

        self._fallback_surface = Surface((self.size, self.size), flags=0)
        self._fallback_surface.fill(self.color)

        # self.label = zone.name
        self.label = f"max: {zone.capacity} d"
        self.font = font.SysFont(None, 24)
        self.text_color = (0, 0, 0)

        

    @classmethod
    def _get_zones_frames(cls) -> list[list[Surface]]:
        if cls._frame_cache is not None:
            return cls._frame_cache

        sheet = image.load(cls.IMAGE_PATH).convert_alpha()
        sheet_w, sheet_h = sheet.get_size()

        cell_w = sheet_w / cls.FRAME_COLS
        cell_h = sheet_h / cls.FRAME_ROWS

        frames: list[list[Surface]] = []
        for row in range(cls.FRAME_ROWS):
            row_frames: list[Surface] = []
            for col in range(cls.FRAME_COLS):
                x0 = round(col * cell_w)
                x1 = round((col + 1) * cell_w)
                y0 = round(row * cell_h)
                y1 = round((row + 1) * cell_h)
                frame = Surface((x1 - x0, y1 - y0), flags=0).convert_alpha()
                frame.fill((0, 0, 0, 0))
                frame.blit(sheet, (0, 0), area=(x0, y0, x1 - x0, y1 - y0))
                row_frames.append(frame)
            frames.append(row_frames)

        cls._frame_cache = frames
        return frames

    def _get_surface(self) -> Surface:
        try:
            frames = self._get_zones_frames()
        except (PygameError, FileNotFoundError, FileExistsError):
            return self._fallback_surface

        if not frames:
            return self._fallback_surface

        return frames[self.image_coord[1]][self.image_coord[0]]


    def render(self, screen: Surface, camera: Camera) -> None:
        source = self._get_surface()
        src_w, src_h = source.get_size()
        sw = self.size / src_w
        sh = self.size / src_h
        scaled = transform.scale(
            source,
            (int(src_w * sw * camera.zoom), int(src_h * sh * camera.zoom))
        )

        c = (self.coord - Point(camera.x, camera.y)) * camera.zoom
        self.center = c + ((self.size * camera.zoom) // 2)
        screen.blit(
            scaled,
            (c.x, c.y)
        )

        if self.zone.is_start or self.zone.is_end:
            return
        
        text_surface = self.font.render(self.label, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = c.x + (self.size * camera.zoom) // 2
        text_rect.bottom = c.y - 4
        screen.blit(text_surface, text_rect)

    def __repr__(self) -> str:
        return f"Zone({self.coord})"
