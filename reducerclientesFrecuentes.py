#!/usr/bin/python 
import sys 

''' 
Reducer de dineroGastadoPorClientes / Creado por Jose Manuel Cuesta
''' 
subproblema = None
DiaCompra = None
acumulado = 0

for claveValor in sys.stdin:

	linea = claveValor.strip()
	clave, valor = linea.split(";",1)

	if subproblema == None:
		subproblema = clave
	if subproblema == clave:

		if DiaCompra == None or DiaCompra != valor:
			DiaCompra = valor
			acumulado = acumulado + 1
		     
	else: #Cambia el subproblema/persona, analizamos la cantidad de dias
		if acumulado > 4:
			print("%s" % (subproblema))
		subproblema = clave

