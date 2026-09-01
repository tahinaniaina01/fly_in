#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   graph_rendrer.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 13:00:56 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 13:59:00 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from models.graph import Graph
from renderer.zone_renderer import ZoneRenderer
from .camera import Camera
import pygame
from .drone_renderer import DroneRenderer
from models.drone import Drone
from models.state import State, ConnState
from utils.point import Point
from utils.utils import DRONE_SIZE

class GraphRenderer:
    def __init__(self, graph: Graph, drones: list[Drone] = []):
        self.graph = graph
        self.zones = graph.zones
        self.connections = graph.connections
        self.zones_renderer: dict[str, ZoneRenderer] = {}
        self.drones_renderer: list[DroneRenderer] = []
        self.drones = drones
        self.step = 0
        for key, val in self.zones.items():
            self.zones_renderer[key] = ZoneRenderer(val, color=val.color)
        for drone in drones:
            if isinstance(drone.path[0], State):
                initial_zone = drone.path[0].zone
                path: list[Point] = []
                for p in drone.path:
                    c = self.zones_renderer[p.zone.name].center - DRONE_SIZE // 2
                    path.append(c)
                self.drones_renderer.append(
                    DroneRenderer(
                        self.zones_renderer[initial_zone.name].center - DRONE_SIZE // 2,
                        path
                    )
                )

    def render(self, screen: pygame.Surface, camera: Camera) -> None:
        for conn in self.connections.values():
            zone_a, zone_b = conn.zones_names()
            origin_p = (
                self.zones_renderer[zone_a].center.x,
                self.zones_renderer[zone_a].center.y
            )
            end_p = (
                self.zones_renderer[zone_b].center.x,
                self.zones_renderer[zone_b].center.y
            )
            pygame.draw.line(
                screen,
                (0, 0, 0),
                origin_p,
                end_p,
                2
            )
        for zr in self.zones_renderer.values():
            zr.render(screen, camera)
        for drone in self.drones_renderer:
            drone.render(screen, camera)

    def move(self) -> None:
        for drone in self.drones_renderer:
            drone.move()
        

