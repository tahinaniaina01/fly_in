#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   zone_renderer.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 15:29:31 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 16:07:08 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from dataclasses import dataclass
from typing import Any
import pygame

from utils import ZONE_ORIGIN, Point, ZONE_DISTANCE
from .camera import Camera
from models import Zone

class ZoneRenderer:
    def __init__(
        self, zone: Zone,
        color: Any = (255, 0, 0), size: int = 50
    ) -> None:
        if not pygame.font.get_init():
            pygame.font.init()

        self.zone = zone
        self.coord: Point = Point(zone.x, zone.y) * ZONE_DISTANCE + ZONE_ORIGIN
        self.color: Any = color
        self.size: int = size
        self.center: Point = self.coord + (self.size // 2)
        self.surface = pygame.Surface((self.size, self.size))
        if zone.zone_type == "blocked":
            self.color = (0, 0, 0)
        elif zone.zone_type == "normal":
            self.color = (0, 255, 255)
        elif zone.zone_type == "priority":
            self.color = (94, 235, 181)
        elif zone.zone_type == "restricted":
            self.color = (238, 210, 86)
        if zone.is_start:
            self.color = (86, 238, 192)
        if zone.is_end:
            self.color = (233, 86, 238)
        self.surface.fill(self.color)

        self.label = zone.name
        # self.label = f"max: {zone.capacity} d"
        self.font = pygame.font.SysFont(None, 24)
        self.text_color = (0, 0, 0)


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

        if self.zone.is_start or self.zone.is_end:
            return
        
        text_surface = self.font.render(self.label, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = c.x + (self.size * camera.zoom) // 2
        text_rect.bottom = c.y - 4
        screen.blit(text_surface, text_rect)

    def __repr__(self) -> str:
        return f"Zone({self.coord})"
