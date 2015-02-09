#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
from math import ceil

## ESCALADO (REDUCCIÓN) CON ESPERANZA MATEMÁTICA (ASUMIR MULTIPLO DE FILAS Y COLUMNAS)##
def img_scalate(pgm,scalate_rows,scalate_cols):
	
	def img_scalate_down():
		new_pgm,factor,csum,avg,index_new = [[] for x in xrange(scalate_rows)],None,0,0,0
		if float(len(pgm))/scalate_rows == ceil(len(pgm)/scalate_rows):  factor = len(pgm)/scalate_rows
		else: factor = len(pgm)/scalate_rows+1
		for x in range(0,len(pgm),factor):
			for y in range(0,len(pgm[0]),factor):
				csum,avg = 0,0
				for s in xrange(factor):
					for p in xrange(factor): 
						csum += int(pgm[x+s][y+p],16)					
				avg = csum/(factor**2)
				new_pgm[index_new/scalate_rows].append(avg)
				index_new += 1
		return new_pgm
	
	def img_scalate_up():
		print "Build it"
	
	if scalate_rows <= len(pgm): return img_scalate_down()
	else:                       return img_scalate_up()
