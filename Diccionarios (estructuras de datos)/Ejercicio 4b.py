"""Programa que lee por teclado una frase y nos devuelve un diccionario con la cantidad de
apariciones de cada carácter en la cadena."""

# Importación de librerías:

from os import system

# Declaración de variables:

frase = "" # Contendrá la cadena de caracteres a escanear. La tratamos como lista.
letra = "" # El carácter que extraemos de la frase (lista).
dicLetras = {} # Diccionario que contendrá: {"letra": nº apariciones}.

# Programa principal:

system("cls")

frase = input("Teclea la frase a escanear: ")
for letra in frase:
    if letra in dicLetras: # Busca en el diccionario la letra.
        dicLetras[letra] += 1 # Si está, incrementa su valor en 1.
    else:
        dicLetras[letra] = 1 # Si no está, es la primera vez, y le asigna 1.

for letra, numVeces in dicLetras.items():
    if letra != " ":
        print(f"La letra {letra} está {numVeces} en la frase.")
    else:
        print(f"El espacio está {numVeces} veces.")

