import numpy as np
numDatos = int(input("Ingrese la cantidad de valores de la cual quiere sacar la Mediana\n"))
valores = []
for x in range (0,int(numDatos)):
    valor = int(input("Ingrese el valor #:"))
    valores.append(valor)
print(np.median(valores))
