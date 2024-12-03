""" Ejercicio 10a: Script que cuenta palabras dentro de un archivo de texto. Le pasamos como
parámetros:
- archivo -> donde busca las palabras.
- --palabra -> palabra a buscar.
Si no se especifica la palabra, se contarán todas las palabras.
"""
# Importación de librerías
import argparse # Tratamiento de argumentos.
from os import system

# Variables:
palabras = [] # Lista que contendrá las palabras del archivo.
numPalabras = 0 # Contendrá el número de palabras.

# Crear el parser (analizador sintáctico de los parámetros que se pasan)
parser = argparse.ArgumentParser(description="Cuenta palabras dentro de un archivo de texto.")

# Definimos los argumentos o parámetros que se van a pasar al programa:
parser.add_argument(
    "archivo",
    type=str,
    help="El archivo donde se realizará el conteo de palabras."
)
parser.add_argument(
    "-p", "--palabra",
    type=str,
    default="*",
    help="Palabra a buscar dentro del archivo. Si no se especifica, se contarán todas."
)

# Programa principal.
system("cls")

# Parsear los argumentos (análisis de los argumentos)
args = parser.parse_args()

with open(args.archivo, "rt") as miArchivo:
    palabras = miArchivo.read().split() # Contenido del archivo en forma de lista de palabras
    if args.palabra == "*":
        print(f"Se han contado {len(palabras)} palabras en el archivo {args.archivo}")
    else:
        for i in range(len(palabras)):
            if palabras[i] == args.palabra:
                numPalabras += 1
        print(f"Se han contado {numPalabras} apariciones de '{args.palabra}' en el archivo {args.archivo}")


