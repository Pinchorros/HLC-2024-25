"""Programa que utiliza una función que nos devuelva True si un valor
 parámetro está dentro de un rango, que también introduciremos como parámetros.
Si no es así, devolverá False.
"""

# Importación de librerías:
from os import system

# Declaración de variables:
valor = 0 # Contendrá el valor a comprobar.
limInferior = 0 # Límite inferior del intervalo.
limSuperior = 0 # Límite superior del intervalo.

# Definición de funciones:

def rango(valor, limInferior, limSuperior):
    """ Devuelve True o False para un valor pasado como parámetro, si está o no
    dentro del intervalo.
    Formato: rango(valor, limInferior, limSuperior) -> Boolean
    """
    if valor >= limInferior and valor <= limSuperior:
        return True
    else:
        return False

# Programa principal:

system("cls")

valor = input("Número a comprobar: ")
limInferior = input("Teclea el extremo inferior del intervalo: ")
limSuperior = input("Teclea el extremo superior del intervalo: ")

if rango(valor, limInferior, limSuperior):
    print("Está dentro del intervalo.")
else:
    print("No está dentro del intervalo.")
