#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   __init__.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:39:57 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 12:32:12 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .point import Point
from .utils import WIN_HEIGHT, WIN_WIDTH, ZONE_SIZE, ZONE_ORIGIN, ZONE_DISTANCE

__all__ = [
    "Point",
    "WIN_HEIGHT",
    "WIN_WIDTH",
    "ZONE_SIZE",
    "ZONE_ORIGIN",
    "ZONE_DISTANCE"
]
