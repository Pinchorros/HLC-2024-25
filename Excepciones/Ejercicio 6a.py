"""	(Versión con excepciones) Programa que administra el inventario de productos de una tienda.
 El programa debe permitir al usuario realizar las siguientes operaciones:

Añadir un producto: Ingresar el nombre del producto, el precio y la cantidad en stock.
Buscar un producto: Ingresar el nombre de un producto y mostrar su precio y cantidad en stock.
Actualizar la cantidad de un producto: Ingresar el nombre de un producto y cambiar la cantidad en stock.
Eliminar un producto: Ingresar el nombre de un producto y eliminarlo del inventario.
Listar todos los productos: Mostrar todos los productos en el inventario con su precio y cantidad.
Salir del programa.         """


# Importación de librerías:
from os import system

# Declaración de variables:
inventario = {} # Diccionario que contendrá toda la estructura.

# Definición de funciones:

def agregarProducto(): # Opción 1
    nombre = input("¿Qué producto quieres añadir al inventario? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        print(f"El producto '{nombre}' ya está dentro del inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        try:
            precio = float(input("Precio del artículo: "))
            cantidad = int(input("Cantidad de artículos: "))
        except ValueError:
            print(f"Error: El valor introducido no es numérico. Artículo {nombre} no añadido.")
        else:
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            print(f"El producto '{nombre}' ha sido añadido a la lista.")
        
        print("")
        input("Pulsa una tecla para continuar...")


def listadoProductos(): # Opción 5.
    print("Listado de los elementos...")
    for nombre, valor in inventario.items(): # Recorro todo el diccionario principal.
        print(f"Producto: {nombre}, Precio: {valor["precio"]}, Cantidad: {valor["cantidad"]}.")

    print("")
    input("Pulsa una tecla para continuar...")     


def buscarProducto(): # Opción 2.
    nombre = input("¿Qué producto quieres buscar? ")
    nombre = nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        precio = inventario[nombre]["precio"]
        cantidad = inventario[nombre]["cantidad"]
        print(f"Producto: {nombre}, Precio: {precio}, Cantidad stock: {cantidad}")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
    print("")
    input("Pulsa una tecla para continuar...")



def actualizarCantidad(): # Opción 3.
    nombre = input("¿De qué producto quieres modificar el stock? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        try:
            cantidad = int(input("Introduce la nueva cantidad en stock: "))
        except ValueError:
            print(f"La cantidad introducida no es numérica. No se puede actualizar el artículo {nombre}.")
        else:
            inventario[nombre]["cantidad"] = cantidad
            print(f"El producto '{nombre}' ha actualizado correctamente su stock a {cantidad} unidades.")
        print("")
        input("Pulsa una tecla para continuar...")



def eliminarProducto(): # Opción 4.
    nombre = input("¿Qué producto quieres eliminar? ")
    nombre = nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        if inventario[nombre]["cantidad"] == 0:
            del inventario[nombre]
            print(f"El producto '{nombre}' ha sido eliminado del inventario.")
        else:
            print(f"No se puede eliminar el producto '{nombre}' ya que su stock no es 0.")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
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
        try:
            opcion = int(input("Elige la opción correspondiente... "))
        except ValueError:
            continue # Se vuelve otra vez al principio del bucle y reescribe el menú

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