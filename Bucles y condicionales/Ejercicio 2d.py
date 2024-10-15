"""Programa que pide por teclado la nota de un examen y muestra por pantalla
Si está aprobado o suspenso (>=5)"""

# Declaración de variables.

calificacion = 0

# Programa principal.

calificacion = float(input("Introduce la calificación del examen: "))

if calificacion >= 5:
    print("¡¡Estás aprobado!!")
else:
    print("Estás suspenso. Nos vemos el próximo año ;-)")

