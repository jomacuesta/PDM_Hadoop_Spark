#!/usr/bin/python
import sys
from pyspark import SparkContext, SparkConf
'''
Programa creado por Jose Manuel Cuesta
Cantidad de gastos < y > 1500 por persona cuyo metodo de pago sea con T.Credito
'''
#LIBRERIA DE FUNCIONES

def getkeyValueRDD(linea):
	paresClaveValor = []
	persona,metodo,cantidad = linea.split(";",2)

	if metodo.upper() == 'TARJETA DE CREDITO':
		claveValor = (persona,int(cantidad))
		paresClaveValor.append(claveValor)
	else:
		claveValor = (persona,0)
		paresClaveValor.append(claveValor)

	return paresClaveValor

def getless1500(linea):
	
	num_pagos = 0
	lista_cantidades = linea[1]
	for elem in lista_cantidades:
		if elem < 1500 and elem > 0:
			num_pagos = num_pagos + 1
	
	return "%s;%d" % (linea[0],num_pagos)

def getmore1500(linea):
	
	num_pagos = 0
	lista_cantidades = linea[1]
	for elem in lista_cantidades:
		if elem > 1500:
			num_pagos = num_pagos + 1
	
	return "%s;%d" % (linea[0],num_pagos)

#inicializacion
conf = SparkConf().setMaster("local").setAppName("personaYMetodosDePago")
sc = SparkContext(conf = conf)
entrada = sys.argv[1]
salida = sys.argv[2]

#cargamos los datos de entrada
RDDinput = sc.textFile(entrada)

#Realizamos construccion de K,V , agrupamos por K y guardamos en cache
RDDcache = RDDinput.flatMap(getkeyValueRDD).groupByKey().mapValues(list).cache()
#Construimos RDDless1500 Y RDDmore1500
RDDless1500 = RDDcache.map(getless1500)
RDDmore1500 = RDDcache.map(getmore1500)

#guardamos las salida
RDDmore1500.saveAsTextFile(salida+ '_a')
RDDless1500.saveAsTextFile(salida+ '_b')

