#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   camera.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 13:10:58 by trakotos            #+#    #+#            #
#   Updated: 2026/06/15 14:35:12 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from dataclasses import dataclass


@dataclass
class Camera:
    x: int = 0
    y: int = 0
    zoom: float = 1.0
    max_zoom: float = 50
    min_zoom: float = 0.1
    velocity: int = 5

    def move(self, dx: int, dy: int) -> None:
        self.x += dx * self.velocity
        self.y += dy * self.velocity

    def zoom_in(self) -> None:
        if self.zoom > 1:
            if self.zoom < self.max_zoom:
                self.zoom += 0.1
        elif self.zoom <= 1:
            self.zoom += 0.01
        else:
            self.zoom = 0.1

    def zoom_out(self) -> None:
        if self.zoom <= 1 and self.zoom > 0.1:
            if self.zoom > self.min_zoom:
                self.zoom -= 0.01
        elif self.zoom > 1:
            self.zoom -= 0.1
        else:
            self.zoom = 0.1

    def __repr__(self) -> str:
        return f"Camera(x={self.x}, y={self.y}, zoom={self.zoom})"
