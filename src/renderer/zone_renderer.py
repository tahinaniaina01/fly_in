#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   zone_renderer.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 15:29:31 by trakotos            #+#    #+#            #
#   Updated: 2026/06/16 14:45:49 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from dataclasses import dataclass
from typing import Any
import pygame

from utils import ZONE_ORIGIN, Point
from .camera import Camera


class ZoneRenderer:
    def __init__(
        self, x: int = 0, y: int = 0,
        color: Any = (255, 0, 0), size: int = 50
    ) -> None:
        self.coord: Point = Point(x, y) * 100 + ZONE_ORIGIN
        self.color: Any = color
        self.size: int = size
        self.center: Point = self.coord + (self.size // 2)
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(self.color)

    def render(self, screen: pygame.Surface, camera: Camera) -> None:
        self.surface = pygame.transform.scale(
            self.surface,
            (self.size * camera.zoom, self.size * camera.zoom)
        )
        c = (self.coord - Point(camera.x, camera.y)) * camera.zoom
        self.center = c + ((self.size * camera.zoom) // 2)
        screen.blit(
            self.surface,
            (c.x, c.y)
        )

    def __repr__(self) -> str:
        return f"Zone({self.coord})"
