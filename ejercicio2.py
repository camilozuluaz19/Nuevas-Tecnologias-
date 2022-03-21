#Leer el nombre de 10 frutas para hacer un salpicon:
#el programa debe permitir mostrar las 10 frutas ingresadas 
#al mismo tiempo en sentido inverso

frutas = []

for i in range (10):
    fruta = input("Ingrese una fruta: ")
    frutas.append(fruta)
    print(frutas)
    
frutas2 = [fruta for fruta in reversed (frutas)]
print(frutas2)