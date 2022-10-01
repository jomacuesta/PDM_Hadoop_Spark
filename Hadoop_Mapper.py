# -*- coding: utf-8 -*-
"""
@author: jcuesta
"""

import sys



if __name__ == "__main__":
    
      for linea in sys.stdin:
        
        linea = linea.strip()
        registro = linea.split(";",3)
        usuario = registro[0]
        orden = registro[3]
        cantidad = registro[2]
        if orden == 'Cierto':
            cantidad = "-" + cantidad
        print("%s %s" % (usuario,cantidad))
        
        