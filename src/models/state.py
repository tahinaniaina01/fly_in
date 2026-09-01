#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   state.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/31 17:23:07 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 16:17:07 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from dataclasses import dataclass
from models.zone import Zone
from models.connection import Connection

@dataclass
class State:
    turn: int
    zone: Zone

    def __hash__(self) -> int:
        id = f"{self.turn}-{self.zone}"
        return hash(id)

@dataclass
class ConnState:
    turn: int
    conn: Connection

    def __hash__(self) -> int:
        id = f"{self.turn}-{self.conn}"
        return hash(id)