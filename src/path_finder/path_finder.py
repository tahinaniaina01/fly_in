#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   path_finder.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 13:03:54 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 11:18:49 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from __future__ import annotations
from dataclasses import dataclass
from .reservations import Reservation
from models.graph import Graph
from models.zone import Zone
from models.connection import Connection
from heapq import heappop, heappush
from models.state import State, ConnState


@dataclass
class PathFinder:
    graph: Graph
    reservations = Reservation()

    def get_path(self, start_time: int = 0) -> list[State | ConnState]:
        
        if (
            self.graph is None or
            self.graph.start_zone is None or
            self.graph.start_zone is None
        ):
            raise Exception("invalid graph")
        visited: set[State] = set()
        heap: list[tuple[int, int, int, Zone]] = [
            (start_time, 0, 0, self.graph.start_zone)
        ]
        counter = 1
        previous: dict[State, State] = {}
        
        while heap:
            turn, cost, _, zone = heappop(heap)
            cur_state = State(turn, zone)
            if cur_state in visited:
                continue
            visited.add(cur_state)

            if zone == self.graph.end_zone:
                return self._construct_path(
                    State(start_time, self.graph.start_zone),
                    cur_state,
                    previous
                )

            counter = self._try_to_wait(
                visited, heap, previous, cur_state, cost, counter
            )
            counter = self._try_to_move(
                visited, heap, previous, cur_state, cost, counter
            )

        raise Exception("Path not found")

    def _try_to_wait(
        self,
        visited: set[State],
        heap: list[tuple[int, int, int, Zone]],
        previous: dict[State, State],
        cur_state: State,
        cost: int,
        counter: int
    ) -> int:
        next_state = State(cur_state.turn + 1, cur_state.zone)
        if next_state in visited:
            return counter
        if not self.reservations.is_free(next_state.turn, next_state.zone):
            return counter
        if next_state not in previous:
            previous[next_state] = cur_state
            heappush(heap, (next_state.turn, cost, counter, next_state.zone))
            counter += 1
        return counter

    def _try_to_move(
        self,
        visited: set[State],
        heap: list[tuple[int, int, int, Zone]],
        previous: dict[State, State],
        cur_state: State,
        cost: int,
        counter: int
    ) -> int:
        conns = self.graph.links(cur_state.zone)
        for conn in conns:
            other = conn.other(cur_state.zone)
            if other is None:
                other = cur_state.zone
            next_state = State(
                cur_state.turn + cur_state.zone.zone_type.path_weight,
                other
            )
            if next_state in visited:
                continue
            if (
                not self.reservations.is_free(next_state.turn, conn) or
                not self.reservations.is_free(next_state.turn, next_state.zone)
            ):
                continue
            if next_state not in previous:
                previous[next_state] = cur_state
                c = cost + next_state.zone.zone_type.mouvement_cost
                heappush(
                    heap, 
                    (next_state.turn, c, counter, next_state.zone)
                )
                counter += 1
        return counter

    def _construct_path(self, start: State, end: State, previous: dict[State, State]) -> list[State | ConnState]:
        paths: list[State | ConnState] = [end]
        cur: State = end
        while cur != start:
            n = cur
            cur = previous[cur]
            paths.append(cur)
            if n.zone != cur.zone:
                conn = self.graph.get_connection(n.zone, cur.zone)
                self.reservations.reserve(n.turn, conn)
            self.reservations.reserve(cur.turn, cur.zone)
        paths.reverse()
        return paths
