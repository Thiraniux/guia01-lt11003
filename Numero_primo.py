
residuo = 0
contador = 1

numero = input("Ingrese un numero\n")

for x in range (1,int(numero)):
    residuo= int(numero) % x
    if (residuo==0):
        contador=contador+1
        print(contador)
if (contador == 2):
    print("Es un numero Primo")
else:
    print("No es un numero Primo")




