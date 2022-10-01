#!/usr/bin/python
import sys
from pyspark import SparkContext, SparkConf
'''
Programa creado por Jose Manuel Cuesta / Gastos realizados diferentes a T.Credito
'''
#LIBRERIA DE FUNCIONES

def getkeyValueRDD(linea):
	paresClaveValor = []
	persona,metodo,cantidad = linea.split(";",2)

	if metodo.upper() != 'TARJETA DE CREDITO':
		claveValor = (persona,int(cantidad))
		paresClaveValor.append(claveValor)
	else:
		claveValor = (persona,0)
		paresClaveValor.append(claveValor)

	return paresClaveValor

def getAcumPersona(acum,valor):
	return acum+valor

def formatL(linea):
	return "%s;%d" % (linea[0],linea[1])

#inicializacion
conf = SparkConf().setMaster("local").setAppName("personaGastosSinTarjetaCredito")
sc = SparkContext(conf = conf)
entrada = sys.argv[1]
salida = sys.argv[2]

#cargamos los datos de entrada
RDDinput = sc.textFile(entrada)

#Realizamos Transformaciones
RDDoutput = RDDinput.flatMap(getkeyValueRDD).reduceByKey(getAcumPersona).map(formatL)

#guardamos la salida
RDDoutput.saveAsTextFile(salida)
