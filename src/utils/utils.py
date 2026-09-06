#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   utils.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:40:03 by trakotos            #+#    #+#            #
#   Updated: 2026/09/06 15:34:34 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .point import Point

WIN_WIDTH = 1920
WIN_HEIGHT = 1080
ZONE_DISTANCE = 400
ZONE_SIZE = 200
ZONE_ORIGIN = Point(
    WIN_WIDTH // 5 - ZONE_SIZE // 2,
    WIN_HEIGHT // 2 - ZONE_SIZE // 2,
)
DRONE_SIZE = 50

