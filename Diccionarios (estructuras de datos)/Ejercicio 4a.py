"""Utilizando diccionarios: se pide por teclado una serie de asignaturas, con su calificación
correspondiente, hasta que introduzca una asignatura en blanco. Posteriormente nos debe mostrar
por pantalla la lista de las que están aprobadas (calificación mayor o igual que 5), con su
correspondiente nota y la media aritmética de todas las calificaciones (se incluirán también
las notas suspensas en la media)."""

# Importación de librerías:

from os import system

# Declaración de variables:

asignatura = " " # Contendrá el nombre de la asignatura (tipo cadena).
calificacion = 0 # Nota de la asignatura (tipo float)-
dicAsignaturas = {} # Diccionario con {"Nombre de asignatura": calificación}.
sumaCalificaciones = 0 # Suma de las notas para hacer, al final, la media aritmética.""

# Programa principal:

system("cls")
while(asignatura != ""):
    asignatura = input("Introduce el nombre de la asignatura (ENTER para finalizar):")
    if asignatura != "":
        calificacion = float(input("Teclea su calificación: "))
        dicAsignaturas[asignatura] = calificacion
    print("") # Hago un salto de línea.
    
for asignaturo, nota in dicAsignaturas.items():
    if nota >= 5:
        print(f"La asignatura {asignaturo} está aprobada con un {nota}.")
    sumaCalificaciones = sumaCalificaciones + nota

print(f"La media aritmética de las calificaciones es {sumaCalificaciones/len(dicAsignaturas)}")


