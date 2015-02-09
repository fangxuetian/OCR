#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

def img_binarization(pgm):
	for row in xrange(len(pgm)):
		# Ajustar el color mínimo [127] empíricamente #
		for col in xrange(len(pgm[0])): pgm[row][col] = 0x00 if pgm[row][col]<=127 else 255
	return pgm
