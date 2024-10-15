"""Programa que pide por teclado números, hasta que introduzca el 0.
 Posteriormente, debe mostrar su suma y su producto."""

# Declaración de variables:

numero = 1 # Valor numérico que voy a pedir por teclado (Puede tener cualquier valor que no sea 0)
suma = 0 # Contendrá la suma de todos los valores metidos por teclado.
producto = 1 # Debe almacenar la multiplicación de todos los números.

# Programa principal:

while numero != 0:
    suma = suma + numero
    producto = producto * numero
    numero = float(input("Introduce el número, por favor (0 para terminar): "))

print(f"La suma es {suma-1} y la multiplicación es {producto}")

