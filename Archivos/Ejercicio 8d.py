""" Crear un programa que consiste en leer un archivo de texto, convertir 
el contenido a mayúsculas y escribir el resultado en un nuevo archivo."""

# Importación de librerías:
from os import system

# Declaración de variables:

contenidoArchivo = " " # Contendrá la frase a línea que se leerá del archivo.

# Definición de funciones:


# Programa principal:

system("cls")

with open("./Archivos/entrada.txt", "rt") as miArchivo:
    print("Abriendo archivo entrada en modo lectura.txt")
    contenidoArchivo = miArchivo.read()
    print(contenidoArchivo)
    contenidoArchivo = contenidoArchivo.upper()

with open("./Archivos/salida.txt", "wt") as miArchivo:
    print("Abriendo archivo salida en modo escritura.txt")
    miArchivo.write(contenidoArchivo)
    print(contenidoArchivo)


    
