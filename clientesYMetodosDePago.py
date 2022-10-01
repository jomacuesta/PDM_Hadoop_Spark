#!/usr/bin/python
import sys
from pyspark import SparkContext, SparkConf
'''
Programa creado por Jose Manuel Cuesta
Numero de pagos con metodos distintos por persona
'''
#LIBRERIA DE FUNCIONES

def getkeyValueRDD(linea):
	
	persona,metodo,cantidad = linea.split(";",2)

	return (persona,metodo)


def countMetodos(linea):
	
	num_metodos = len(list(linea[1]))
	if num_metodos > 1:
		varios_metodos = 'Cierto'
	else:
		varios_metodos = 'Falso'
	
	return "%s;%s" % (linea[0],varios_metodos)

#inicializacion
conf = SparkConf().setMaster("local").setAppName("clientesYMetodosDePago")
sc = SparkContext(conf = conf)
entrada = sys.argv[1]
salida = sys.argv[2]

#cargamos los datos de entrada
RDDinput = sc.textFile(entrada)

#Realizamos las transformaciones
RDDoutput = RDDinput.map(getkeyValueRDD).distinct().groupByKey().map(countMetodos)

#guardamos las salida
RDDoutput.saveAsTextFile(salida)


