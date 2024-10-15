"""Crea un programa que simule una lista de compras. El programa debe permitir al usuario
 realizar las siguientes operaciones:
1.- Agregar un artículo a la lista de compras.
2.- Eliminar un artículo de la lista de compras.
3.- Mostrar los artículos que están actualmente en la lista.
4.- Salir del programa."""

from os import system

# Declaración de variables:

listaCompra = [] # Lista que contendrá los artículos.
opcion = 0 # Contendrá el valor elegido por el usuario en el menú.
articulo = "" # Contendrá el texto correspondiente al artículo de la compra.

# Programa principal:

while opcion != 4:
    system("cls")
    print("") # Salto de línea para dejar una línea en blanco.
    print("***************   MENÚ PRINCIPAL  ****************")
    print("1.- Agregar un artículo a la lista de la compra.")
    print("2.- Eliminar un artículo a la lista de la compra.")
    print("3.- Mostar todos los artículos de la lista de la compra.")
    print("4.- Salir del programa")
    print("")
    opcion = int(input("Elige la opción correspondiente... "))

    if opcion == 1: # Añadir un elemento a la lista (append).
        print("")
        articulo = input("Teclea un nuevo artículo para la lista de la compra: ")
        articulo = articulo.capitalize()
        if articulo in listaCompra:
            print(f"El artículo '{articulo}' ya está dentro de la lista.")
            input("Pulsa una tecla para continuar...")
        else:
            listaCompra.append(articulo)
            print(f"El artículo '{articulo}' ha sido añadido a la lista.")
            input("Pulsa una tecla para continuar...")

    elif opcion == 2: # Eliminar un elemento de la lista (remove).
        print("Borrando un elemento...")
        input("Pulsa una tecla para continuar...")
        

    elif opcion == 3: # Mostrar un listado de todos los elementos de la lista.
        print("Listado de los elementos...")
        input("Pulsa una tecla para continuar...")


