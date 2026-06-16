#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   map_parser.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/02 11:22:01 by trakotos            #+#    #+#            #
#   Updated: 2026/06/16 14:30:04 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from dataclasses import dataclass, field
from models import Graph, Zone, Connection, ZoneType


class ParseError(Exception):
    def __init__(self, nu_line: int, message: str) -> None:
        super().__init__(f"Error on line {nu_line}: {message}")


@dataclass
class Parser:
    graph: Graph = field(default_factory=Graph)
    nb_drones: int | None = None

    def parse(self, file_name: str) -> tuple[int | None, Graph]:
        lines: list[str] = []
        with open(file_name, "r") as f:
            lines = f.readlines()

        for line_nu, line_val in enumerate(lines):
            line = line_val.strip().split("#", 1)
            if not line[0]:
                continue
            if self._parse_nb_drones(line_nu, line[0]):
                continue
            if self._parse_zone(line_nu, line[0]):
                continue
            if self._parse_connection(line_nu, line[0]):
                continue
            raise ParseError(line_nu, "Invalid syntax")

        return (self.nb_drones, self.graph)

    def _parse_nb_drones(self, line_nu: int, line: str) -> bool:
        if self.nb_drones is None:
            if line.startswith("nb_drones:"):
                n = line.split(':', 1)[1].strip()
                try:
                    num = int(n)
                    self.nb_drones = num
                except Exception as e:
                    raise ParseError(line_nu + 1, str(e))
            else:
                raise ParseError(
                    line_nu + 1,
                    "The first line must be nb_drones: <number>"
                )
            return True
        return False

    def _parse_zone(self, line_nu: int, line: str) -> bool:
        if (
            line.startswith("start_hub:") or
            line.startswith("end_hub:") or
            line.startswith("hub:")
        ):
            val = line.split(':', 1)[1].strip().split()
            if len(val) < 3:
                raise ParseError(line_nu + 1, "Invalid zone")

            name, x, y = val[:3]
            props = " ".join(val[3:]).strip("[]")

            try:
                x_coord = int(x)
                y_coord = int(y)
            except ValueError:
                raise ParseError(line_nu + 1, "Invalid zone")

            color: str | None = None
            max_drones: int | None = None
            zone_type: ZoneType = ZoneType.NORMAL
            for prop in props.split():
                if "=" not in prop:
                    continue
                key, value = prop.split("=", 1)
                value = value.strip("[]")
                if key == "color":
                    color = value
                elif key == "max_drones":
                    try:
                        max_drones = int(value)
                    except ValueError:
                        raise ParseError(line_nu + 1, "Invalid zone")
                elif key == "zone":
                    try:
                        zone_type = ZoneType(value)
                    except ValueError:
                        raise ParseError(line_nu, f"unknown zone type {value}")

            is_start = line.startswith("start_hub")
            is_end = line.startswith("end_hub")
            zone = Zone(
                name,
                x_coord,
                y_coord,
                color=color,
                max_drones=max_drones if max_drones is not None else 1,
                is_start=is_start,
                zone_type=zone_type,
                is_end=is_end,
            )
            self.graph.add_zone(zone)
            return True
        return False

    def _parse_connection(self, line_nu: int, line: str) -> bool:
        if line.startswith("connection:"):
            label = line.split(":", 1)[1].strip().split()[0].strip()
            if "-" not in label:
                raise ParseError(line_nu + 1, "Invalid connection")

            zone_a_name, zone_b_name = label.split("-", 1)
            print((zone_a_name, zone_b_name))
            try:
                zone_a = self.graph.zones[zone_a_name]
                zone_b = self.graph.zones[zone_b_name]
            except KeyError:
                raise ParseError(line_nu + 1, "Unknown zone in connection")
            conn = Connection(zone_a, zone_b)
            self.graph.add_connection(conn)

            return True
        return False
