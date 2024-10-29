""" Programa que utiliza una función para devolver el módulo de un vector
de 3 dimensiones"""

# Importación de librerías:
from os import system

# Declaración de variables:
CoordX = 0
CoordY = 0
CoordZ = 0
modulo = 0 # Contendrá el módulo del vector que pido por teclado.

# Definición de funciones:

def modulo3D(coordX, coordY, coordZ):
    """Devuelve el módulo del vector de 3 dimensiones.
    Formato: modulo3D(coordenada X, coordenada Y, coordenada Z)."""
    resultado = (coordX**2+coordY**2+coordZ**2)**0.5
    return resultado

# Programa principal:

system("cls")

coordX = float(input("Introduce la coordenada X del vector: "))
coordY = float(input("Introduce la coordenada Y del vector: "))
coordZ = float(input("Introduce la coordenada Z del vector: "))

modulo = modulo3D(coordX, coordY, coordZ)
print(f"El módulo del vector ({coordX}, {coordY}, {coordZ}) es {modulo}.")

