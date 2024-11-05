"""	(Versión con módulos)Programa que administra el inventario de productos de una tienda.
 El programa debe permitir al usuario realizar las siguientes operaciones:

Añadir un producto: Ingresar el nombre del producto, el precio y la cantidad en stock.
Buscar un producto: Ingresar el nombre de un producto y mostrar su precio y cantidad en stock.
Actualizar la cantidad de un producto: Ingresar el nombre de un producto y cambiar la cantidad en stock.
Eliminar un producto: Ingresar el nombre de un producto y eliminarlo del inventario.
Listar todos los productos: Mostrar todos los productos en el inventario con su precio y cantidad.
Salir del programa.         """


# Importación de librerías:
from os import system
from archivosModulos.FuncionesInventario import *

# Declaración de variables:
inventario = {} # Diccionario que contendrá toda la estructura.

# Definición de funciones:

def menu():
    opcion = 0
    while opcion != 6:
        system("cls")
        print("") # Salto de línea para dejar una línea en blanco.
        print("***************   MENÚ PRINCIPAL  ****************")
        print("1.- Agregar un producto al inventario.")
        print("2.- Buscar un producto en el inventario.")
        print("3.- Actualizar la cantidad de un producto del inventario.")
        print("4.- Eliminar un producto al inventario.")
        print("5.- Mostar todos los productos del inventario.")
        print("6.- Salir del programa")
        print("")
        try:
            opcion = int(input("Elige la opción correspondiente... "))
        except ValueError:
            continue # Se vuelve otra vez al principio del bucle y reescribe el menú

        if opcion == 1: # Agregar un producto al inventario.
            agregarProducto(inventario)

        elif opcion == 2: # Buscar un producto en el inventario..
           buscarProducto(inventario)
        
        elif opcion == 3: #  Actualizar la cantidad de un producto del inventario.
            actualizarCantidad(inventario)

        elif opcion == 4: #  Eliminar un producto al inventario.
            eliminarProducto(inventario)

        elif opcion == 5: #  Mostar todos los productos del inventario..
            listadoProductos(inventario)





# Programa principal:

menu()