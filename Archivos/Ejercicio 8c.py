""" Escribe un programa que lea el archivo datos.txt del ejercicio anterior,
 y muestre por pantalla el listado de los nombres y edades."""

# Importación de librerías:
from os import system

# Declaración de variables:

linea = " " # Contendrá la frase a línea que se leerá del archivo.

# Definición de funciones:


# Programa principal:

system("cls")

with open("./Archivos/datos.txt", "rt+") as miArchivo:
    print(miArchivo.readlines()) # Guarda las líneas en una lista.
    print(miArchivo.read())
