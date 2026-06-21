#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   app.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 14:14:36 by trakotos            #+#    #+#            #
#   Updated: 2026/06/21 17:05:15 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import pygame
from models.graph import Graph
from .camera import Camera
from .graph_rendrer import GraphRenderer


class App:
    def __init__(self, graph: Graph, w: int = 800, h: int = 600):
        self.running = False
        self.width = w
        self.height = h
        self.screen = None
        self.clock = pygame.time.Clock()
        self.graph = Graph
        self.camera = Camera()
        self.graph_renderer = GraphRenderer(graph)

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYUP:
                if event.key == 32:
                    print("space pressed")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.camera.move(0, -1)
        if keys[pygame.K_DOWN]:
            self.camera.move(0, 1)
        if keys[pygame.K_LEFT]:
            self.camera.move(-1, 0)
        if keys[pygame.K_RIGHT]:
            self.camera.move(1, 0)
        if keys[pygame.K_a]:
            self.camera.zoom_in()
        if keys[pygame.K_z]:
            self.camera.zoom_out()
        if keys[pygame.K_q]:
            self.running = False

    def display(self) -> None:
        if self.screen is None:
            return
        self.screen.fill(pygame.Color(255, 255, 255))
        self.graph_renderer.render(self.screen, self.camera)

    def update(self):
        pygame.display.flip()

    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        while self.running:
            self.handle_event()
            self.display()
            self.update()
            self.clock.tick(60)

        pygame.quit()
