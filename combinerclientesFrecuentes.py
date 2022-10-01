#!/usr/bin/python 
import sys 

''' 
Combiner clientesFrecuentes - Objetivo: Reducir la carga de datos
Creado por Jose Manuel Cuesta
''' 
subproblema = None
DiaCompra = None

for claveValor in sys.stdin:
	
	linea = claveValor.strip()
	clave,valor = linea.split(";",1)

	if subproblema == None:
		subproblema = clave	
		DiaCompra = valor
		print("%s;%s" % (subproblema,DiaCompra))
	if subproblema == clave:

		if valor == DiaCompra:
			continue
		else:
			DiaCompra = valor
			print("%s;%s" % (subproblema,DiaCompra))
	else:
		subproblema = clave
		DiaCompra = valor
		print("%s;%s" % (subproblema,DiaCompra))



