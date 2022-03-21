#Construir un programa que permita ingresar N(cantidad digitada por el usuario)
#numeros enteros y cuente cuantos multipos de 2 y de 3 fueron ingresados 

numeros = []
cantidadNumeros = int(input("Digite la cantidad de numeros: "))

for i in range (cantidadNumeros):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)

for numero in numeros:
    if(numero % 2 == 0 and numero % 3 == 0):
        print(numero)