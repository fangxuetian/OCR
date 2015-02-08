#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.



def img_extract_rows(fd):
	rows = []
	for line in fd.readlines():
		btes = line.split()
		rows.append([hex(int(x)) for x in btes])
	return rows


#def save_ppm(fd,ppm,rows,cols,whitest):
	
