#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

# min_rows y min_cols deben ser los mínimos de entre todas las imagenes del corpus #

def norm_aspect_ratio(ppm,min_rows,min_cols,bgcolor):
	rows_added = 0
	while len(ppm) < min_rows:
		ppm.insert(0,[row for row in [bgcolor for x in xrange(min_cols)]])
		rows_added += 1
	for x in range(rows_added,len(ppm)):
		while len(ppm[x]) < min_cols: ppm[x].append(bgcolor)
	return ppm
