#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   graph.py                                             :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 12:59:07 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 10:44:19 by trakotos           ###   ########.fr      #
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

    def links(self, zone: Zone) -> list[Connection]:
        conns = []
        for conn in self.connections.values():
            if conn.include(zone):
                conns.append(conn)
        return conns

    def get_connection(self, zone1: Zone, zone2: Zone) -> Connection:
        t = ("", "")
        if zone1.name < zone2.name:
            t = (zone1.name, zone2.name)
        else:
            t = (zone2.name, zone1.name)
        key = f"{t[0]}-{t[1]}"
        return self.connections[key]

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
