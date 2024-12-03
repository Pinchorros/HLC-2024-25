""" Ejercicio 10c: Script que cambia la extension de varios archivos. Le pasamos como parámetros:
- carpeta -> carpeta de trabajo, donde se van a buscar los archivos.
- --extension_inicial -> extensión de los archivos a cambiar.
- --extension_final -> extensión de los archivos a poner.
"""
# Importación de librerías
import argparse # Tratamiento de argumentos.
from os import system, listdir

# Variables:
archivos = [] # Lista que va a contener todos los archivos del directorio

# Crear el parser (analizador sintáctico de los parámetros que se pasan)
parser = argparse.ArgumentParser(description="Renombrado de extensiones de archivo.")

# Definimos los argumentos o parámetros que se van a pasar al programa:
parser.add_argument(
    "carpeta",
    type=str,
    help="Carpeta que contiene a los archivos."
)
parser.add_argument(
    "-ei", "--extension_inicial",
    type=str,
    help="Extensión de los archivos a cambiar."
)
parser.add_argument(
    "-ef", "--extension_final",
    type=str,
    help="Extensión de los archivos a poner."
)

# Programa principal.
system("cls")

# Parsear los argumentos (análisis de los argumentos)
args = parser.parse_args()

archivos = listdir(args.carpeta)
print(f"Lista de archivos antes de cambiar la extensión {archivos}.")
for i in range(len(archivos)):
    if "."+args.extension_inicial in archivos[i]:
        print("He encontrado una extensión")
        archivos[i] = archivos[i].replace("."+ args.extension_inicial, "."+ args.extension_final)

print(f"Lista de archivos después de cambiar la extensión {archivos}.")

# Falta por cambiar los nombres de archivo en el SO

