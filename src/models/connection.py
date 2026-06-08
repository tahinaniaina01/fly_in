#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   connection.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 11:20:06 by trakotos            #+#    #+#            #
#   Updated: 2026/06/08 12:44:11 by trakotos           ###   ########.fr      #
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

    @property
    def label(self) -> str:
        if self.zone_a.name < self.zone_b.name:
            a, b = (self.zone_a, self.zone_b)
        else:
            a, b = (self.zone_b, self.zone_a)
        return f"{a.name}-{b.name}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Connection):
            return NotImplemented
        return value == self.label
