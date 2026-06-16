#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   graph_rendrer.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 13:00:56 by trakotos            #+#    #+#            #
#   Updated: 2026/06/16 14:45:28 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from models.graph import Graph
from renderer.zone_renderer import ZoneRenderer
from .camera import Camera
import pygame
from random import randint


class GraphRenderer:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.zones = graph.zones
        self.connections = graph.connections
        self.zone_renderers: dict[str, ZoneRenderer] = {}
        for key, val in self.zones.items():
            self.zone_renderers[key] = ZoneRenderer(x=val.x, y=val.y)

    def render(self, screen: pygame.Surface, camera: Camera) -> None:
        for conn in self.connections.values():
            zone_a, zone_b = conn.zones_names()
            origin_p = (
                self.zone_renderers[zone_a].center.x,
                self.zone_renderers[zone_a].center.y
            )
            end_p = (
                self.zone_renderers[zone_b].center.x,
                self.zone_renderers[zone_b].center.y
            )
            pygame.draw.line(
                screen,
                (0, 0, 255),
                origin_p,
                end_p,
                2
            )
        for zr in self.zone_renderers.values():
            zr.render(screen, camera)
