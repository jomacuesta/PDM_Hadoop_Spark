#!/usr/bin/python 
import sys 
''' 
Combiner de Patents / Creado por Jose Manuel Cuesta - 03MBID - PDM
''' 
citador = None
lista_citados = []
#Por cada registro creamos  <citador,lista_citados> 

for linea in sys.stdin: 
	linea = linea.strip() 
	clave,valor = linea.split(",", 1)
	clave = int(clave)
	valor = int(valor)
	if citador == None: 
		citador = clave
	if citador == clave:
		lista_citados = sorted(lista_citados + [valor])
	else:
	   	print("%d,%s" % (citador,str(lista_citados)))
		citador = clave
		lista_citados = [valor]

print("%d,%s" % (citador,str(lista_citados)))
