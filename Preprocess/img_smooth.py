#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

# Suavizado por esperanza matemática de los k-vecinos más cercanos a un pixel dado #
# ASUMIR k MULTIPLO DE FILAS Y COLUMNAS #
def img_smooth(pgm,k):
	avg = 0
	for x in xrange(len(pgm)):
		for y in xrange(len(pgm[0])):
			avg_neighbors = extract_k_neighbors_avg(pgm,x,y,k)
			pgm[x][y]     = avg_neighbors[0]/avg_neighbors[1] if avg_neighbors[1]!=0 else 0
	return pgm

# Vecinos en cruz (no da buenos resultados), arreglar #	
def extract_k_neighbors_avg(pgm,x,y,k):
	sum_neighbors   = 0
	right_neighbors = pgm[x][y-(k/2):y]
	left_neighbors  = pgm[x][y:y+(k/2)]
	up_neighbors    = [pgm[s][y] for s in range(x-(k/2),x) if (x-(k/2))>0]
	down_neighbors  = [pgm[s][y] for s in range(x,x+(k/2)) if (x+(k/2))<len(pgm)]
	if right_neighbors != []: sum_neighbors += reduce(lambda x,y: x+y,right_neighbors)
	if left_neighbors  != []: sum_neighbors += reduce(lambda x,y: x+y,left_neighbors)
	if up_neighbors    != []: sum_neighbors += reduce(lambda x,y: x+y,up_neighbors)
	if down_neighbors  != []: sum_neighbors += reduce(lambda x,y: x+y,down_neighbors)
	return (sum_neighbors,len(right_neighbors)+len(left_neighbors)+len(up_neighbors)+len(down_neighbors))
				
	
