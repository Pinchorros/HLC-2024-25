


# Importación de librerías:
from os import system

# Declaración de variables:
inventario = {} # Diccionario que contendrá toda la estructura.

# Definición de funciones:

def agregarProducto():
    nombre = input("¿Qué producto quieres añadir al inventario? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        print(f"El producto '{nombre}' ya está dentro del inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        precio = float(input("Precio del artículo: "))
        cantidad = int(input("Cantidad de artículos: "))
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print(f"El producto '{nombre}' ha sido añadido a la lista.")
        print("")
        input("Pulsa una tecla para continuar...")


def listadoProductos():
    print("Listado de los elementos...")
    for nombre, valor in inventario.items(): # Recorro todo el diccionario principal.
        print(f"Producto: {nombre}, Precio: {valor["precio"]}, Cantidad: {valor["cantidad"]}.")

    print("")
    input("Pulsa una tecla para continuar...")     


def actualizarCantidad():
    nombre = input("¿De qué producto quieres modificar el stock? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        cantidad = int(input("Introduce la nueva cantidad en stock: "))
        inventario[nombre]["cantidad"] = cantidad
        print(f"El producto '{nombre}' ha actualizado correctamente su stock a {cantidad} unidades.")
        print("")
        input("Pulsa una tecla para continuar...")

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
        opcion = int(input("Elige la opción correspondiente... "))

        if opcion == 1: # Agregar un producto al inventario.
            agregarProducto()

        elif opcion == 2: # Buscar un producto en el inventario..
           buscarProducto()
        
        elif opcion == 3: #  Actualizar la cantidad de un producto del inventario.
            actualizarCantidad()

        elif opcion == 4: #  Eliminar un producto al inventario.
            eliminarProducto()

        elif opcion == 5: #  Mostar todos los productos del inventario..
            listadoProductos()





# Programa principal:

menu()

