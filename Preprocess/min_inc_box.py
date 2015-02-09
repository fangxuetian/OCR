#!/usr/bin/env python
# -*- encoding: 850 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

def get_box_coords(pgm,bgcolor):
	left_col,right_col,top_row,down_row = float('inf'),-float('inf'),float('inf'),-float('inf')
	for row in xrange(len(pgm)):
		for col in xrange(len(pgm[0])):
			if pgm[row][col] != bgcolor:
				if row < top_row:   top_row    = row
				if row > down_row:  down_row   = row
				if col < left_col:  left_col   = col
				if col > right_col: right_col  = col
	return [top_row,down_row,left_col,right_col]
						
def min_inc_box(pgm,bgcolor):
	box_coords = get_box_coords(pgm,bgcolor)
	new_pgm    = []
	for row in range(box_coords[0],box_coords[1]+1):
		new_pgm.append([])
		for col in range(box_coords[2],box_coords[3]+1):
			new_pgm[row-box_coords[0]].append(pgm[row][col])
	return new_pgm
