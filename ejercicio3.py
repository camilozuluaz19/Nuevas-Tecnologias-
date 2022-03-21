#Construir un programa para ir de compras a un supermercado

import math


print("SuperMercado Don Baraton")
print("****")
print("1, Digita 1 Recibir codigo, nombre, precio")
print("2, Digita 2 para mostrar los productos registrados ")
print("3, Digita 3 para permitir buscar por codigo un producto y editar el precio  ")
print("4, Digita 4 para permitir buscar por codigo un producto y eliminar el producto")
print("0, Digita 0 para salir")
print("****")


opcion = 1
productos = []
producto = {}

while(opcion != 0):
    opcion = int(input("Digita una opcion: "))

    if(opcion == 0):
        break
    elif(opcion == 1):
       producto['codigo'] = input("Digite el codigo del producto: ")
       producto['nombre'] = input("Digite el nombre del producto: ")
       producto['precio'] = int(input("Digite el precio del producto: "))
       productos.append(producto)
       producto = {}
    elif(opcion == 2):
        print(productos)
    elif(opcion == 3):
        buscar = input("Ingrese el codigo a buscar: ")
        for producto in productos:
            if(buscar == producto['codigo']):
               precioEditar = producto['precio']
               print(producto)
               producto['precio'] = int(input(f"Digite el Precio del producto {precioEditar}: "))
            else:
                print("El producto no existe")
    elif(opcion == 4):
             eliminarProducto = input("Ingrese el codigo del producto que busca: ")
             for producto in productos:
               if(eliminarProducto == producto['codigo']): 
                   del eliminarProducto                
                   print("El Producto fue Elimininado Exitosamente")
            

    elif(opcion == 0):
        break

        