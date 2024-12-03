""" Ejercicio 10b: Script que convierte unidades. Le pasamos como parámetros:
- valor -> valor numérico a convertir de una unidad a otra.
- --unidad_inicial -> unidades en las que está el valor pasado.
- --unidad_final -> unidades a las que convertir el valor.
"""
# Importación de librerías
import argparse # Tratamiento de argumentos.
from os import system

# Variables:


# Crear el parser (analizador sintáctico de los parámetros que se pasan)
parser = argparse.ArgumentParser(description="Conversión de unidades.")

# Definimos los argumentos o parámetros que se van a pasar al programa:
parser.add_argument(
    "valor",
    type=float,
    help="Valor a convertir de una unidad a otra"
)
parser.add_argument(
    "-ui", "--unidad_inicial",
    type=str,
    help="Unidad desde la que convertir {km, m, cm}"
)
parser.add_argument(
    "-uf", "--unidad_final",
    type=str,
    help="Unidad a la que convertir {km, m, cm}"
)

# Programa principal.
system("cls")

# Parsear los argumentos (análisis de los argumentos)
args = parser.parse_args()

if args.unidad_inicial == args.unidad_final:
    print("La unidad de partida coincide con la final!!")
    exit() # Salgo del programa

if args.unidad_inicial == "km" and args.unidad_final == "m": # km a m.
    print(f"{args.valor} {args.unidad_inicial} son {args.valor*1000} {args.unidad_final}.")
elif args.unidad_inicial == "m" and args.unidad_final == "km": # m a km.
    print(f"{args.valor} {args.unidad_inicial} son {args.valor/1000} {args.unidad_final}.")
elif args.unidad_inicial == "m" and args.unidad_final == "cm": # m a cm.
    print(f"{args.valor} {args.unidad_inicial} son {args.valor*100} {args.unidad_final}.")
elif args.unidad_inicial == "m" and args.unidad_final == "km": # cm a m.
    print(f"{args.valor} {args.unidad_inicial} son {args.valor/100} {args.unidad_final}.")
elif args.unidad_inicial == "km" and args.unidad_final == "cm": # km a cm.
    print(f"{args.valor} {args.unidad_inicial} son {args.valor*100000} {args.unidad_final}.")
elif args.unidad_inicial == "cm" and args.unidad_final == "km": # cm a km.
    print(f"{args.valor} {args.unidad_inicial} son {args.valor/100000} {args.unidad_final}.")