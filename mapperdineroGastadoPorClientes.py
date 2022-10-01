#!/usr/bin/python 
import sys 

''' 
Mapper de dineroGastadoPorlientes 
Creado por Jose Manuel Cuesta - 03MBID - PDM
''' 

#Por cada registro creamos  <persona,cantidad> con valor negativo si es devolucion 
for linea in sys.stdin: 
	linea = linea.strip() 
	persona, producto, cantidad, esDevolucion = linea.split(";", 3)

	if esDevolucion == 'Falso':
		cantidad = int(cantidad)
	else:
		cantidad = -int(cantidad)
	 
	print("%s;%s" % (persona, cantidad)) 
