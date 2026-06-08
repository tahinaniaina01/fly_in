#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   map_parser.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/02 11:22:01 by trakotos            #+#    #+#            #
#   Updated: 2026/06/08 14:14:44 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from dataclasses import dataclass
from models import Graph


class ParseError(Exception):
    def __init__(self, nu_line: int, message: str) -> None:
        super().__init__(f"Error on line {nu_line}: {message}")


@dataclass
class Parser:
    graph = Graph()
    nb_drones: None | int = None

    def parse(self, file_name: str) -> None:
        lines: list[str] = []
        with open(file_name, "r") as f:
            lines = f.readlines()

        for line_nu, line_val in enumerate(lines):
            line = line_val.strip().split("#", 1)
            if not line[0]:
                print(f"empty line or comment in line {line_nu + 1}")
                continue
            if self._parse_nb_drones(line_nu, line[0]):
                continue

    def _parse_nb_drones(self, line_nu: int, line: str) -> bool:
        if self.nb_drones is None:
            if line.startswith("nb_drones:"):
                n = line.split(':', 1)[0]
                try:
                    num = int(n)
                    self.nb_drones = num
                except Exception as e:
                    raise ParseError(line_nu, str(e))
            else:
                raise ParseError(
                    line_nu + 1,
                    "The first line must be nb_drones: <number>"
                )
            return True
        return False

    def _parse_zone(self, line_nu: int, line: str) -> bool:
        if line.startswith("start_hub:"):
            val = line.split(':')[1].strip().split()
            val_len = len(val)
            if val_len != 4 and val_len != 3:
                raise ParseError(line_nu, "invalid zone")
            name, x, y, prop = val
            if not x.isdecimal() or not y.isdecimal():
                raise ParseError(line_nu, "Invalid zone")
        return False
