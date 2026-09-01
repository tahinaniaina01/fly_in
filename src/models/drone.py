#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   drone.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/31 09:35:57 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 12:16:03 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from .zone import Zone
from .state import State, ConnState
from dataclasses import dataclass

@dataclass
class Drone:
    id: int
    path: list[State | ConnState]

