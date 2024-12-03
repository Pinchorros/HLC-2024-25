# archivo: busqueda.py
import argparse
import os

# Crear el parser
parser = argparse.ArgumentParser(description="Busca archivos en un directorio dado con un patrón específico.")

# Definir los argumentos
parser.add_argument(
    "directorio",
    type=str,
    help="El directorio donde se realizará la búsqueda"
)

parser.add_argument(
    "-p", "--patron",
    type=str,
    default="*",
    help="Patrón de archivo a buscar (ejemplo: *.txt)"
)

parser.add_argument(
    "-r", "--recursivo",
    action="store_true",
    help="Si se incluye, se realiza una búsqueda recursiva en subdirectorios"
)

# Parsear los argumentos
args = parser.parse_args()

# Función para buscar archivos
def buscar_archivos(directorio, patron, recursivo):
    print(f"Buscando archivos en '{directorio}' con el patrón '{patron}' {'de forma recursiva' if recursivo else ''}.\n")
    # Si se especifica búsqueda recursiva
    if recursivo:
        for root, _, files in os.walk(directorio):
            for file in files:
                if file.endswith(patron.replace("*", "")):
                    print(f"Encontrado: {os.path.join(root, file)}")
    else:
        # Si no es recursivo, solo buscar en el directorio dado
        for file in os.listdir(directorio):
            if file.endswith(patron.replace("*", "")):
                print(f"Encontrado: {os.path.join(directorio, file)}")

# Ejecutar la función de búsqueda
buscar_archivos(args.directorio, args.patron, args.recursivo)
