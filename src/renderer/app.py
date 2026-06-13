#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   app.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 14:14:36 by trakotos            #+#    #+#            #
#   Updated: 2026/06/09 13:35:40 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import pygame
from models.graph import Graph
from typing import Any
from random import randint

class App:
    def __init__(self, graph: Graph, w: int = 600, h: int = 400):
        self.running = False
        self.width = w
        self.height = h
        self.screen = None
        self.clock = pygame.time.Clock()
        self.graph = Graph
        self.grid: list[Any] = []

    def _init(self):
        for _ in range(8):
            tmp = []
            for _ in range(12):
                s = pygame.Surface((50, 50))
                s.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
                tmp.append(s)
            self.grid.append(tmp)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.screen.fill(pygame.Color(255, 255, 255))
        

    def display(self):
        pygame.display.update()

    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        while self.running:
            self.handle_event()
            self.update()
            self.display()
            self.clock.tick(60)

        pygame.quit()
