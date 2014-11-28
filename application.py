# -*- coding: utf-8 -*-
""" Este programa da resultado factorial """
print        """
                 88      a8P          db         88b           d88  
                 88    ,88'          d88b        888b         d888  
                 88  ,88"           d8'`8b       88`8b       d8'88  
                 88,d88'           d8'  `8b      88 `8b     d8' 88  
                 8888"88,         d8YaaaaY8b     88  `8b   d8'  88  
                 88P   Y8b       d8        8b    88   `8b d8'   88  
                 88     "88,    d8'        `8b   88    `888'    88  
                 88       Y8b  d8'          `8b  88     `8'     88  
                                                                   """
factor = 0

def factorizacion(num):
    i = 1
    while num > 0:
        i = i *(num)
        num = num - 1
    print "Su resultado factorial es: "
    return i

while True:
    factor = raw_input("Ingrese Número: ")
    try:
        factor = int(factor)
        if factor > 0:
            break
        else:
            print u"Ingresar un número entero positivo\n"
    except(TypeError, NameError, ValueError):
        print u"Ingrese un número entero positivo\n"
        RESPUESTA = True

print factorizacion(factor)
