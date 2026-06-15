#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   graph_rendrer.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/15 13:00:56 by trakotos            #+#    #+#            #
#   Updated: 2026/06/15 13:05:25 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from models.graph import Graph
import pygame


class GraphRenderer:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.zones = graph.zones
        self.connections = graph.connections

    def render(self, screen: pygame.Surface) -> None:
        pass
