#!/usr/bin/env python
# -*- encoding: 850 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import ppm_utils
import norm_asp_ratio # TEST PURPOSE #
import img_scal       # TEST PURPOSE #

def get_box_coords(ppm,bgcolor):
	left_col,right_col,top_row,down_row = float('inf'),-float('inf'),float('inf'),-float('inf')
	for row in xrange(len(ppm)):
		for col in xrange(len(ppm[0])):
			if ppm[row][col] != bgcolor:
				if row < top_row:   top_row    = row
				if row > down_row:  down_row   = row
				if col < left_col:  left_col   = col
				if col > right_col: right_col  = col
	return [top_row,down_row,left_col,right_col]
						
def min_inc_box(ppm,bgcolor):
	box_coords = get_box_coords(ppm,bgcolor)
	new_ppm    = []
	for row in range(box_coords[0],box_coords[1]+1):
		new_ppm.append([])
		for col in range(box_coords[2],box_coords[3]+1):
			new_ppm[row-box_coords[0]].append(ppm[row][col])
	return new_ppm



## ENDPOINT PARA TEST EN LA PRIMERA ETAPA DEL PREPROCESO ##
if __name__ == "__main__":
	with open("1.pgm","rb") as fd:
		header     = fd.readline()
		size       = fd.readline().split(" ")
		cols,rows  = int(size[0]),int(size[1])
		whitest    = hex(int(fd.readline())) 
		ppm        = ppm_utils.img_extract_rows(fd)		
		bgcolor    = '0xff'
		ppm        = min_inc_box(ppm,bgcolor)
		print "Tamanyo de la caja de minima inclusion: " + str(len(ppm)),'x',str(len(ppm[0]))
		## ASUMIR MINIMOS DE FILAS Y COLUMNAS ##
		ppm        = norm_asp_ratio.norm_aspect_ratio(ppm,10,10,'0xff')
		print "Tamanyo despues de normalizacion del aspect ratio: " + str(len(ppm)),'x',str(len(ppm[0]))
		img_scal.img_scalate(ppm,5,5)
		
	fd.close()
