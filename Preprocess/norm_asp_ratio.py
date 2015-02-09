#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

# min_rows y min_cols deben ser los mínimos de entre todas las imagenes del corpus #

def norm_aspect_ratio(pgm,min_rows,min_cols,bgcolor):
	rows_added,cols_added = 0,0
	while len(pgm) < min_rows:
		if rows_added%2==0: pgm.insert(0,[row for row in [bgcolor for x in xrange(min_cols)]])
		else: pgm.append([row for row in [bgcolor for x in xrange(min_cols)]])
		rows_added += 1
	for x in range(rows_added/2,len(pgm)):
		cols_added = 0
		while len(pgm[x])<min_cols:
			if cols_added%2==0: pgm[x].insert(0,bgcolor)
			else:               pgm[x].append(bgcolor)
			cols_added += 1
	return pgm
