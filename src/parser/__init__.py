#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   __init__.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/02 13:59:34 by trakotos            #+#    #+#            #
#   Updated: 2026/06/02 14:06:36 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .map_parser import Parser

__all__: list[str] = ["Parser"]
