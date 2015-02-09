#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

from norm_asp_ratio import norm_aspect_ratio
from img_scal       import img_scalate  
from img_bin        import img_binarization
from img_smooth     import img_smooth
from pgm_utils      import save_pgm,extract_whitest,img_extract_rows
from min_inc_box    import min_inc_box
from sys            import argv
def fail(msg):
	print msg+"\n"
	print "-> Please, contact with [overxfl0w13 AT hotmail DOT com], or report at:\n\n\t\t* https://github.com/overxfl0w/OCR/issues/new\n"
	return 1

def success(msg): 
	print msg
	return 0

def header():
	"""BROADWAY"""
	print """
	 ___   ___   ____  ___   ___   ___   __    ____  __   __  
	| |_) | |_) | |_  | |_) | |_) / / \ / /`  | |_  ( (` ( (` 
	|_|   |_| \ |_|__ |_|   |_| \ \_\_/ \_\_, |_|__ _)_) _)_) 
	
	""" 

def footer(fail):
	print "-> Preproceso finalizado",
	if fail>0: print "- - -\n\n"
	else:      print "+ + +\n\n"
	
## ENTRY POINT ##
if __name__ == "__main__":
	cfail = 0
	header()
	try:
		with open("1.pgm","rb") as fd:
			header     = fd.readline()
			size       = fd.readline().split(" ")
			cols,rows  = int(size[0]),int(size[1])
			whitest    = hex(int(fd.readline())) 
			pgm        = img_extract_rows(fd)		
			bgcolor    = '0xff'
			try:
				pgm        = min_inc_box(pgm,bgcolor)
				cfail  |= success("-> Tamanyo de la caja de minima inclusion: " + str(len(pgm))+'x'+str(len(pgm[0]))+" + ")
			except Exception as e:
				cfail  |= fail("-> Caja de minima inclusion - ")
			try:
				pgm        = norm_aspect_ratio(pgm,64,64,'0xff')
				cfail  |= success("-> Tamanyo despues de normalizacion del aspect ratio: " + str(len(pgm))+'x'+str(len(pgm[0]))+" + ")
			except Exception as e:
				cfail  |= fail("-> Aspect ratio - ")
			try:
				pgm        = img_scalate(pgm,32,32)
				cfail  |= success("-> Tamanyo despues del escalado: " + str(len(pgm))+'x'+str(len(pgm[0]))+" + ")
			except Exception as e:
				cfail  |= fail("-> Escalado - ")
			try:
				## Smooth por acabar correctitud, resultados no deseados de momento ##	
				#pgm        = img_smooth(pgm,2)
				cfail  |= success("-> Tamanyo despues del suavizado: " + str(len(pgm))+'x'+str(len(pgm[0]))+" + ")
			except Exception as e:
				cfail  |= fail("-> Suavizado - ")
		fd.close()
		try:
			pgm            = img_binarization(pgm)
			cfail  |= success("-> Binarizacion completada "+" + ")
		except Exception as e:
			cfail  |= fail("-> Binarizacion - ")
		try:
			save_pgm("1-2.pgm",pgm,extract_whitest(pgm))
			cfail  |= success("-> Archivo salvado "+" + ")
		except Exception as e:
			cfail  |= fail("-> Salvar archivo - ")
	except:
		cfail  |= fail("-> Abrir archivo - ")
	footer(cfail)
	
