#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   point.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:39:51 by trakotos            #+#    #+#            #
#   Updated: 2026/06/15 14:44:24 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)
