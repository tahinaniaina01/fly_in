#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   reservations.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/31 10:27:18 by trakotos            #+#    #+#            #
#   Updated: 2026/08/31 13:19:55 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from dataclasses import dataclass
from ..models.zone import Zone
from ..models.connection import Connection


@dataclass
class Reservation:
    zone_reservations: dict[tuple[int, Zone], int] = {}
    conn_reservations: dict[tuple[int, Connection], int] = {}

    def reserve(self, t: int, data: Zone | Connection) -> None:
        if isinstance(data, Zone):
            key = (t, data)
            if key in self.zone_reservations.keys():
                self.zone_reservations[key] += 1
            else:
                self.zone_reservations[key] = 1
        elif isinstance(data, Connection):
            key = (t, data)
            if key in self.conn_reservations.keys():
                self.conn_reservations[key] += 1
            else:
                self.conn_reservations[key] = 1
        else:
            raise TypeError("incompatible type, required Zone | Connection")

    def is_free(self, t: int, data: Zone | Connection) -> bool:
        if isinstance(data, Zone):
            key = (t, data)
            if self.zone_reservations[key] < data.max_drones:
                return True
            return False
        elif isinstance(data, Connection):
            key = (t, data)
            if self.conn_reservations[key] < data.max_link_capacity:
                return True
            return False
        return False

                