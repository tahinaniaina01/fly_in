#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   reservations.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/31 10:27:18 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 10:34:10 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from dataclasses import dataclass, field
from models.zone import Zone
from models.connection import Connection


@dataclass
class Reservation:
    zone_reservations: dict[tuple[int, Zone], int] = field(default_factory=dict)
    conn_reservations: dict[tuple[int, Connection], int] = field(default_factory=dict)

    def reserve(self, t: int, data: Zone | Connection) -> None:
        if isinstance(data, Zone):
            key = (t, data)
            if key in self.zone_reservations.keys():
                self.zone_reservations[key] += 1
            else:
                self.zone_reservations[key] = 1
        elif isinstance(data, Connection):
            conn_key = (t, data)
            if conn_key in self.conn_reservations.keys():
                self.conn_reservations[conn_key] += 1
            else:
                self.conn_reservations[conn_key] = 1
        else:
            raise TypeError("incompatible type, required Zone | Connection")

    def is_free(self, t: int, data: Zone | Connection) -> bool:
        if isinstance(data, Zone):
            key = (t, data)
            if self.zone_reservations.get(key, 0) < data.capacity:
                return True
            return False
        elif isinstance(data, Connection):
            conn_key = (t, data)
            if self.conn_reservations.get(conn_key, 0) < data.max_link_capacity:
                return True
            return False
        return False

    def __repr__(self) -> str:
        return f"conn: {self.conn_reservations} \nzone: {self.zone_reservations}\n"

                