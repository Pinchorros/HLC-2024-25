""" Crea un programa que pida al usuario ingresar varias frases y
 las guarde en un archivo de texto llamado salida.txt. Continuará
solicitando frases hasta que teclee una vacía. Cada una de las
 frases se irá guardando en el archivo anterior.
 Usa la cláusula with open. """

# Importación de librerías:
from os import system

# Declaración de variables:

frase = " " # Contendrá la frase a grabar en el archivo,se pide por teclado.
listaFrases = [] # Lista que contendrá las frases a grabar en el archivo.

# Definición de funciones:


# Programa principal:

system("cls")

while frase != "":
    frase = input("Introduce la frase a grabar en el archivo (ENTER para finalizar): ")
    listaFrases.append(frase)

del listaFrases[-1] # Borra el último elemento
# listaFrases.remove("") # Otra forma de borrar el elemento que contiene "".
print(listaFrases)

with open("./Archivos/salida.txt", "wt") as miArchivo:
    for frase in listaFrases:
        miArchivo.write(frase + "\n")

