#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   app.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 14:14:36 by trakotos            #+#    #+#            #
#   Updated: 2026/06/15 13:11:48 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import pygame
from models.graph import Graph
from .camera import Camera

class App:
    def __init__(self, graph: Graph, w: int = 600, h: int = 400):
        self.running = False
        self.width = w
        self.height = h
        self.screen = None
        self.clock = pygame.time.Clock()
        self.graph = Graph
        self.camera = Camera()
        

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYUP:
                if event.key == 32:
                    print("space pressed")

    def display(self):
        self.screen.fill(pygame.Color(255, 255, 255))
        pass

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
