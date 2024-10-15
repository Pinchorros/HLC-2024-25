"""Pedirá por teclado una palabra y hemos de decir si es
 un palíndromo o no."""

# Declaración de variables:

palabra = "" # Cadena que contendrá la palabra a analizar (para ver si es palíndromo o no).
longitudPalabra = 0 # Contendrá el tamaño de la palabra.
indice = 0 # Índice con el que recorremos la palabra.
palindromo = True # Indica si la palabra es palíndromo o no. 

# Importación de librerías:

from os import system # Importo el comando "system" de la librería "os".

# Programa principal:

system("cls") # Para borrar la pantalla del terminal.
palabra = input("Introduce la palabra para ver si es palíndromo o no: ")
longitudPalabra = len(palabra) - 1 #Le resto 1 porque la lista formada por la palabra comienza en 0.

while indice < longitudPalabra - indice and palindromo == True:
    if palabra[indice] != palabra[longitudPalabra - indice]:
        palindromo = False 
    indice = indice + 1

if palindromo == True:
    print(f"La palabra {palabra} es un palíndromo.")
else:
    print(f"La palabra {palabra} NO es un palíndromo.")





    