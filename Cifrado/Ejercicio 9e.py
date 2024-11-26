""" Mejora del programa de inventario, que graba el diccionario en formato .json.
Le añadimos cifrado el archivo de datos"""

# Importación de librerías:
from os import system
import json # Manipulación de archivos .json
from cryptography.fernet import Fernet


# Declaración de variables:
inventario = {} # Diccionario que contendrá toda la estructura.
clave = "" # Contendrá la clave generada por Fernet, para el cifrado del archivo.


# Definición de funciones:

def cargarClave(): # Función que carga la clave desde el archivo en que se guardó.
        return open("./Cifrado/clave.key", "rb").read()

def descifrar(nombreArchivo, clave):
    """
    Dado un nombre de archivo y clave, descifra el archivo y lo graba."""
    f = Fernet(clave)
    with open(nombreArchivo, "rb") as archivo: # Lee los datos del archivo cifrado
        datosCifrados = archivo.read()
    datos = f.decrypt(datosCifrados) # Descifra los datos
    with open(nombreArchivo, "wb") as archivo: # Escribe los datos en el archivo.
        archivo.write(datos)

def cifrar(nombreArchivo, clave): 
    """Función que dado el nombreArchivo y la clave, cifra el archivo y lo guarda en disco con extensión .cifrado."""
    f = Fernet(clave) # Inicializamos el objeto "Fernet"
    with open(nombreArchivo, "rb") as archivo: # Leemos el contenido del archivo.
        datosArchivo = archivo.read()
    datosCifrados = f.encrypt(datosArchivo) # Ciframos el contenido del archivo.
    with open(nombreArchivo, "wb") as archivo:
        archivo.write(datosCifrados) # Guardamos en disco el archivo, pero con datos cifrados (sobreescribo los datos originales)

def agregarProducto(): #1
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

def buscarProducto(): #2
    nombre = input("¿De que producto quieres ver detalles? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        print(f"Producto: {nombre}, Cantidad: {inventario[nombre]["cantidad"]}, Precio: {inventario[nombre]["precio"]}")
        input("Pulsa una tecla para continuar...")

def actualizarCantidad(): #3
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

def eliminarProducto(): #4
    nombre = input("¿Qué producto quieres eliminar del inventario? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        del[inventario[nombre]]
        input(f"{nombre} fue eliminado. Pulsa una tecla para continuar...")

def listadoProductos(): #5
    if inventario: # Si el inventario no está vacío, contiene elementos.
        print("Listado de los elementos...")
        for nombre, valor in inventario.items(): # Recorro todo el diccionario principal.
            print(f"Producto: {nombre}, Precio: {valor["precio"]}, Cantidad: {valor["cantidad"]}.")
    else:
        print("El inventario está vacío: no hay elementos que mostrar")
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
    
    # Volcamos el contenido del diccionario en el archivo inventario.json

    with open("./Archivos/inventario.json", "w") as miArchivo:
        json.dump(inventario, miArchivo)
    cifrar(miArchivo, clave) # Cifro el archivo .json
 


# Programa principal:

clave = cargarClave() # Cargo la clave de cifrado desde el archivo clave.key
#descifrar("./Archivos/inventario.json", clave) # Descifro el archivo

with open("./Archivos/inventario.json", "r") as miArchivo:
    inventario = json.load(miArchivo)
menu()
