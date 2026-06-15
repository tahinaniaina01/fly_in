#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   app.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 14:14:36 by trakotos            #+#    #+#            #
#   Updated: 2026/06/15 12:50:44 by trakotos           ###   ########.fr      #
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
        self._init()

    def _init(self) -> None:
        for i in range(8):
            tmp: list[Any] = []
            for j in range(12):
                s = pygame.Surface((50, 50))
                s.fill((randint(0, 255), randint(0, 255), randint(0, 255)))
                tmp.append((s, s.get_rect(topleft=(j*50, i*50))))
            self.grid.append(tmp)

    def handle_event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYUP:
                if event.key == 32:
                    print("space pressed")

    def display(self):
        self.screen.fill(pygame.Color(255, 255, 255))
        for i in range(8):
            for j in range(12):
                self.screen.blit(self.grid[i][j][0], self.grid[i][j][1])

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
