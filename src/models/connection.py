#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   connection.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 11:20:06 by trakotos            #+#    #+#            #
#   Updated: 2026/06/16 14:23:22 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from dataclasses import dataclass, field
from .zone import Zone


@dataclass
class Connection:
    zone_a: Zone
    zone_b: Zone
    max_link_capacity: int = field(default=1)

    def zones_names(self) -> tuple[str, str]:
        if self.zone_a.name < self.zone_b.name:
            return (self.zone_a.name, self.zone_b.name)
        return (self.zone_b.name, self.zone_a.name)

    @property
    def label(self) -> str:
        a, b = self.zones_names()
        return f"{a}-{b}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Connection):
            return NotImplemented
        return value.label == self.label
