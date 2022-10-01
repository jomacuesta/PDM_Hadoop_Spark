#!/usr/bin/python 
import sys 

''' 
Reducer de dineroGastadoPorClientes
Creado por Jose Manuel Cuesta
''' 

subproblema = None
acumulado = 0

for claveValor in sys.stdin:
	persona, cantidad_registro = claveValor.split(";",1)

	cantidad_registro = int(cantidad_registro)
	if subproblema == None:
		subproblema = persona

	if subproblema == persona:
		acumulado = acumulado + cantidad_registro

	else:
		print("%s;%s" % (subproblema, acumulado))
		subproblema = persona
		acumulado = cantidad_registro

print("%s;%s" % (subproblema, acumulado))

