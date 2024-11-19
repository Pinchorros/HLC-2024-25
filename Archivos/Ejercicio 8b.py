""" Escribe un programa que pida por teclado el nombre y edad de personas 
y los vaya guardando en un archivo llamado datos.txt, con
 el formato “nombre, edad.” """

# Importación de librerías:
from os import system

# Declaración de variables:

nombre = " " # Contendrá la frase a grabar en el archivo,se pide por teclado.
edad = 0 # Variable para la edad de la persona
listaPersonas = [] # Lista que contendrá las los nombres y edades contatenadas.

# Definición de funciones:


# Programa principal:

system("cls")

with open("./Archivos/datos.txt", "wt") as miArchivo:
    while nombre != "":
        nombre = input("Introduce el nombre de la persona (ENTER para finalizar): ")
        if nombre != "":
            edad = input("Introduce la edad de la persona: ")
            listaPersonas.append(nombre + ", " + edad + ".")
            miArchivo.write(listaPersonas[-1] + "\n") # Grabo en el archivo el último elemento de la lista.
    print("Archivo datos.txt grabado correctamente!!")
        
