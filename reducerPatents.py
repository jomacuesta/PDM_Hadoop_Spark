#!/usr/bin/python 
import sys
import ast 
''' 
Reducer de Patents / Creado por Jose Manuel Cuesta - 03MBID - PDM
''' 
citador = None
lista_citados = []
#Por cada registro creamos  <citador,lista_citados> 

for linea in sys.stdin: 

	linea = linea.strip() 
	clave,valor = linea.split(",", 1)
	lista_valor = ast.literal_eval(valor)

	if citador == None: 
		citador = clave
	if citador == clave:
		lista_citados = sorted(lista_citados + lista_valor)

	else:
	   	print("%s   %s" % (citador,str(lista_citados)[1:-1]))
		citador = clave
		lista_citados = lista_valor

print("%s   %s" % (citador,str(lista_citados)[1:-1]))

