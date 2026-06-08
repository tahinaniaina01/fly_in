#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   zone.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 10:29:24 by trakotos            #+#    #+#            #
#   Updated: 2026/06/08 18:10:49 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from enum import Enum
from dataclasses import dataclass, field


class ZoneType(str, Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"

    @property
    def mouvement_cost(self) -> int:
        costs: dict[ZoneType, int] = {
            ZoneType.PRIORITY: 1,
            ZoneType.NORMAL: 1,
            ZoneType.RESTRICTED: 2,
            ZoneType.BLOCKED: 0
        }
        return costs[self]

    @property
    def path_weight(self) -> int:
        weight: dict[ZoneType, int] = {
            ZoneType.PRIORITY: 1,
            ZoneType.NORMAL: 2,
            ZoneType.RESTRICTED: 4,
            ZoneType.BLOCKED: 9999
        }
        return weight[self]



@dataclass
class Zone:
    name: str
    x: int
    y: int
    color: str | None = field(default=None)
    zone_type: ZoneType = field(default=ZoneType.NORMAL)
    max_drones: int = field(default=1)
    is_start: bool = field(default=False)
    is_end: bool = field(default=False)

    @property
    def capacity(self) -> int:
        if self.is_start or self.is_end:
            import sys

            return sys.maxsize
        return self.max_drones

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Zone):
            raise NotImplementedError()
        return self.name == value.name

    def __repr__(self) -> str:
        return self.name
