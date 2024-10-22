"""Programa que crea un diccionario simulando una cesta de la compra. El programa
debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
que el usuario decida terminar. Después se debe mostrar por pantalla la lista de
la compra y el coste total."""

# Importación de librerías:

from os import system

# Declaración de variables:

nombreArticulo = " " # Contiene el nombre del artículo a comprar (por teclado).
precioArticulo = "" # Precio del artículo (se pide por teclado.)
dicArticulos = {} # Diccionario con formato {"nombre de artículo": precio de artículo}.
sumaCompra = 0 # Valor total de la suma de la compra.

# Programa principal:

system("cls")
while(nombreArticulo != ""):
    nombreArticulo = input("Introduce el nombre del artículo a añadir a la cesta de la compra (ENTER para finalizar): ")
    if nombreArticulo != "":
        precioArticulo = float(input("Teclea su precio: "))
        dicArticulos[nombreArticulo] = precioArticulo
    print("") # Hago un salto de línea.

for nombreArticulo, precioArticulo in dicArticulos.items():
    print(f"Artículo: {nombreArticulo}, precio: {precioArticulo}")
    sumaCompra += precioArticulo # Equivale a sumaCompra = sumaCompra + precioArticulo

print(f"El importe total de la compra es {sumaCompra}.")
