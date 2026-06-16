#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   utils.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 14:40:03 by trakotos            #+#    #+#            #
#   Updated: 2026/06/16 13:42:41 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .point import Point

WIN_WIDTH = 800
WIN_HEIGHT = 600

ZONE_SIZE = 50
ZONE_ORIGIN = Point(
    WIN_WIDTH // 5 - ZONE_SIZE // 2,
    WIN_HEIGHT // 2 - ZONE_SIZE // 2,
)
