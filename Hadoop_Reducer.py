# -*- coding: utf-8 -*-

"""
@author: jcuesta
"""
import sys




if __name__ == "__main__":

    subproblema = None
    acumulado = 0
	
    for claveValor in sys.stdin:
         
        usuario,cantidad = claveValor.split()
        cantidad = float(cantidad)
        
        if subproblema == None:
            subproblema = usuario
            acumulado = cantidad
            
        elif subproblema == usuario:
            acumulado += cantidad
            
        else:
            print("%s %s" %  (subproblema,acumulado))
            subproblema = usuario
            acumulado = 0
            
    print("%s %s" % (subproblema,acumulado))
