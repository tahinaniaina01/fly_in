#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 13:12:18 by trakotos            #+#    #+#            #
#   Updated: 2026/09/01 13:04:27 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from renderer import App
from sys import argv
from parser import Parser
from utils import WIN_HEIGHT, WIN_WIDTH
from path_finder.path_finder import PathFinder
from models.drone import Drone

if __name__ == '__main__':
    if len(argv) != 2:
        print("ERROR: usage python src/main.py <maps.txt>")
        exit(1)
    parser = Parser()
    try:
        nb_drones, graph = parser.parse(argv[1])
        if nb_drones is None:
            raise Exception("missing nb_drones")
        print(f"nombres de drones: {nb_drones}\n")
        path_finder = PathFinder(graph)
        drones = []

        for i in range(1, nb_drones + 1):
            path = path_finder.get_path()
            drone = Drone(i, path)
            drones.append(drone)
            for p in path:
                print(p)
            print()
        app = App(graph, drones, WIN_WIDTH, WIN_HEIGHT)
        app.run()
        # print(graph)
    except Exception as err:
        print(err)
