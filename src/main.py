#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 13:12:18 by trakotos            #+#    #+#            #
#   Updated: 2026/06/15 14:52:21 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from renderer import App
from sys import argv
from parser import Parser
from utils import WIN_HEIGHT, WIN_WIDTH


if __name__ == '__main__':
    if len(argv) != 2:
        print("ERROR: usage python src/main.py <maps.txt>")
        exit(1)
    parser = Parser()
    try:
        nb_drones, graph = parser.parse(argv[1])
        print(f"nombres de drones: {nb_drones}")
        print(graph)
    except Exception as err:
        print(err)

    app = App(graph, WIN_WIDTH, WIN_HEIGHT)
    app.run()
