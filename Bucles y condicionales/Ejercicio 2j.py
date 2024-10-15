"""(Uso de la estructura “elif”) Pide por teclado un valor
entre 1 y 7 y debe indicarnos por pantalla el día de
la semana correspondiente."""

# Declaración de variables:
diaSemana = 0 # Contiene el valor numérico del ordena del día de la semana.

# Programa principal:

diaSemana = int(input("Teclea el número del día de la semana (1 - 7): "))

if diaSemana == 1:
    print("El día introducido en LUNES.")
elif diaSemana == 2:
    print("El día introducido en MARTES.")
elif diaSemana == 3:
    print("El día introducido en MIÉRCOLES.")
elif diaSemana == 4:
    print("El día introducido en JUEVES.")
elif diaSemana == 5:
    print("El día introducido en VIERNES.")
elif diaSemana == 6:
    print("El día introducido en SÁBADO.")
elif diaSemana == 7:
    print("El día introducido en DOMINGO.")    