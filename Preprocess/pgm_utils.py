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


def save_pgm(fname,pgm,whitest):
	with open(fname,"wb") as fd:
		fd.write("P2\n")
		fd.write(str(len(pgm[0]))+" "+str(len(pgm))+"\n")
		fd.write(str(whitest)+"\n")
		for row in pgm:
			for col in row: fd.write(str(col)+" ")
			fd.write("\n")
	fd.close()
	
def extract_whitest(pgm):
	whitest = -float('inf')
	for row in pgm:
		for col in row: whitest = col if col > whitest else whitest
	return whitest
