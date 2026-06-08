#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/01 13:12:18 by trakotos            #+#    #+#            #
#   Updated: 2026/06/02 14:07:25 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# from renderer import App
from sys import argv
from parser import Parser

if __name__ == '__main__':
    if len(argv) != 2:
        print("ERROR: usage python src/main.py <maps.txt>")
        exit(1)
    parser = Parser()
    parser.parse(argv[1])
