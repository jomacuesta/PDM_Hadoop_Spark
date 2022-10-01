#!/usr/bin/python 
import sys 

''' 
Mapper de Patents
Creado por Jose Manuel Cuesta - 03MBID - PDM
''' 

#Por cada registro creamos  <citador,citado> 
for linea in sys.stdin: 
	linea = linea.strip() 
	clave,valor = linea.split(",", 1)
	if clave.isdigit() and valor.isdigit(): 
		print("%s,%s" % (clave,valor))
	else:
		continue 
