#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   graph.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 12:59:07 by trakotos            #+#    #+#            #
#   Updated: 2026/06/16 14:20:32 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .zone import Zone
from .connection import Connection
from dataclasses import dataclass, field


@dataclass
class Graph:
    zones: dict[str, Zone] = field(default_factory=dict)
    connections: dict[str, Connection] = field(default_factory=dict)
    start_zone: Zone | None = field(default=None)
    end_zone: Zone | None = field(default=None)

    def add_zone(self, zone: Zone) -> None:
        if zone.name in self.zones:
            raise ValueError(f"Duplicate zone {zone.name}")
        self.zones[zone.name] = zone

    def add_connection(self, conn: Connection) -> None:
        if conn.label in self.connections.keys():
            raise ValueError(f"Duplicate connection {conn.label}")
        self.connections[conn.label] = conn

    def __repr__(self):
        res = "Zones:\n"
        for key, val in self.zones.items():
            res += f"\t{key}: {val}\n"
        res += "\n"
        res += "Connection:\n"
        for key, val in self.connections.items():
            res += f"\t{key}: {val}\n"
        res += "\n"
        return res
