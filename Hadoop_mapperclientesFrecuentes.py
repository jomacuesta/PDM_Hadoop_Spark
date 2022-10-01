#!/usr/bin/python 
import sys 

''' 
Mapper de clientesFrecuentes 
Creado por Jose Manuel Cuesta - 03MBID - PDM
''' 

#Por cada registro creamos  <persona,dia> 
for linea in sys.stdin: 
	linea = linea.strip() 
	persona, dia, cantidad = linea.split(";", 2) 
	print("%s;%s" % (persona,dia)) 
