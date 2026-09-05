#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   drone_renderer.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/01 12:25:02 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 16:38:23 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from utils import Point
from typing import Any
from pygame import Surface, transform
from .camera import Camera
from models.state import State, ConnState
from utils.utils import DRONE_SIZE
from time import time

class DroneRenderer:
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
        self.surface = Surface((self.size, self.size))
        self.surface.fill(self.color)
        self.is_moving = False
        self._move_start = self.coord
        self._move_end: Point = self.coord
        self._start_time = 0.0
        self._move_duration = 0.5
        self.path: list[Point] = path
        print(path)



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
        if not self.is_moving:
            return

        elpased = time() - self._start_time
        t = min((elpased / self._move_duration), 1.0)

        self.coord = self._move_start + (self._move_end - self._move_start) * t

        if t >= 1.0:
            self.coord = self._move_end
            self.is_moving = False

    def render(self, screen: Surface, camera: Camera) -> None:
        self.update()
        self.surface = transform.scale(
            self.surface,
            (self.size * camera.zoom, self.size * camera.zoom)
        )
        c = (self.coord - Point(camera.x, camera.y)) * camera.zoom
        self.center = c + ((self.size * camera.zoom) // 2)
        screen.blit(
            self.surface,
            (c.x, c.y)
        )
        