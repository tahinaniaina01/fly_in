#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   point.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:39:51 by trakotos            #+#    #+#            #
#   Updated: 2026/06/16 13:31:54 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from dataclasses import dataclass
from typing import Any

@dataclass
class Point:
    x: float = 0
    y: float = 0

    def __add__(self, other: Any) -> Point:
        if not (
            isinstance(other, int) or
            isinstance(other, float) or
            isinstance(other, Point)
        ):
            raise ValueError("Incompatible type")
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return Point(self.x + other, self.y + other)

    def __sub__(self, other: Any) -> Point:
        if not (
            isinstance(other, int) or
            isinstance(other, float) or
            isinstance(other, Point)
        ):
            raise ValueError("Incompatible type")
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return Point(self.x - other, self.y - other)

    def __mul__(self, other: Any):
        if not (
            isinstance(other, int) or
            isinstance(other, float) or
            isinstance(other, Point)
        ):
            raise ValueError("Incompatible type")
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other: Any):
        if not (
            isinstance(other, int) or
            isinstance(other, float) or
            isinstance(other, Point)
        ):
            raise ValueError("Incompatible type")
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return Point(self.x + other, self.y + other)
