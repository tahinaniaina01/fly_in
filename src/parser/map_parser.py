#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   map_parser.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/02 11:22:01 by trakotos            #+#    #+#            #
#   Updated: 2026/06/03 09:26:18 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class ParseError(Exception):
    def __init__(self, nu_line: int, message: str) -> None:
        super().__init__(f"Error on line {nu_line}: {message}")


class Parser:
    def __init__(self) -> None:
        pass

    def parse(self, file_name: str) -> None:
        lines: list[str] = []
        try:
            with open(file_name, "r") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e}")
        for line_nu, line_val in enumerate(lines):
            line = line_val.split("#", 1)
            if not line[0]:
                print(f"empty line or comment in line {line_nu}")
                continue
            print(line[0], end="")
