"""Programa que lee por teclado 2 números y diga
cuál es mayor (supondremos que son diferentes)"""

# Declaración de variables:

primerNumero = 0
segundoNumero = 0

# Programa principal:

primerNumero = float(input("Teclea al primer número: "))
segundoNumero = float(input("Introduce el segundo número: "))

# Esta forma de hacerlo es más difícil de leer y entender.
"""if primerNumero > segundoNumero:
    print(f"El primer número, que es {primerNumero}, es MAYOR que el segundo, {segundoNumero}.")
else:
    if primerNumero == segundoNumero:
        print(f"El primer número, que es {primerNumero}, es IGUAL que el segundo, {segundoNumero}.")
    else:
        print(f"El primer número, que es {primerNumero}, es MENOR que el segundo, {segundoNumero}.")
"""

# Esta forma es mejor, utilizando la estructura "elif".
if primerNumero > segundoNumero:
    print(f"El primer número, que es {primerNumero}, es MAYOR que el segundo, {segundoNumero}.")
elif primerNumero == segundoNumero:
    print(f"El primer número, que es {primerNumero}, es IGUAL que el segundo, {segundoNumero}.")
else:
    print(f"El primer número, que es {primerNumero}, es MENOR que el segundo, {segundoNumero}.")
