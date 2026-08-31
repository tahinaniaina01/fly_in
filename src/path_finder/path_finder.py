#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   path_finder.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 13:03:54 by trakotos            #+#    #+#            #
#   Updated: 2026/08/31 16:44:11 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from dataclasses import dataclass
from .reservations import Reservation
from ..models.graph import Graph
from ..models.zone import Zone
from ..models.connection import Connection
from heapq import heappop, heappush


@dataclass
class State:
    turn: int
    zone: Zone

@dataclass
class PathFinder:
    graph: Graph
    reservations = Reservation()

    def get_path(self, start_time: int = 0) -> list[State]:
        visited: set[State] = set()
        heap: list[tuple[int, int, Zone]] = [
            (start_time, 0, self.graph.start_zone)
        ]
        counter = 1
        previous: dict[State, State] = {}
        

        while heap:
            _, turn, zone = heappop(heap)
            cur_state = State(turn, zone)
            if cur_state in visited:
                continue
            visited.add(cur_state)

            if zone == self.graph.end_zone:
                # return path
                return []

            counter = self._try_to_wait(
                visited, heap, previous, cur_state, counter
            )

            
        raise Exception("Path not found")

    def _try_to_wait(
        self,
        visited: set[State],
        heap: list[tuple[int, int, Zone]],
        previous: dict[State, State],
        cur_state: State,
        counter: int
    ) -> int:
        next_state = State(cur_state.turn + 1, cur_state.zone)
        if next_state in visited:
            return counter
        if not self.reservations.is_free(next_state.turn, next_state.zone):
            return counter
        if next_state not in previous:
            previous[next_state] = cur_state
            heappush(heap, (next_state.turn, counter, next_state.zone))
        return counter

    def _try_to_move(
        self,
        visited: set[State],
        heap: list[tuple[int, int, Zone]],
        previous: dict[State, State],
        cur_state: State,
        counter: int
    ) -> int:
        if cur_state in visited:
            return counter
        next_state = State(cur_state.turn + 1, cur_state.zone)
        if not self.reservations.is_free(next_state.turn, next_state.zone):
            return counter
        if next_state not in previous:
            previous[next_state] = cur_state
            heappush(heap, (next_state.turn, counter, next_state.zone))
        return counter