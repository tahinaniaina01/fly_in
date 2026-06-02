#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   app.py                                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 14:14:36 by trakotos            #+#    #+#            #
#   Updated: 2026/06/01 16:41:53 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import pygame


class App:
    def __init__(self, w: int = 800, h: int = 600):
        self.running = False
        self.width = w
        self.height = h
        self.screen = None

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def display(self):
        pass

    def run(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        while self.running:
            self.handle_event()
            self.update()
            self.display()

        pygame.quit()
