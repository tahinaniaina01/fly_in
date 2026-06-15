#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   camera.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 13:10:58 by trakotos            #+#    #+#            #
#   Updated: 2026/06/15 13:11:15 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Camera:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
        self.zoom = 1

    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def zoom_up(self, dz: int) -> None:
        self.zoom += dz

    def zoom_down(self, dz: int) -> None:
        self.zoom -= dz

    def __repr__(self) -> str:
        return f"Camera(x={self.x}, y={self.y}, zoom={self.zoom})"
