"""(Tuplas) Pide por teclado un valor entre 1 y 7 y debe indicarnos por pantalla
 el día de la semana correspondiente."""

# Declaración de variables:

diaSemana = 0 # Contiene el valor numérico del número del día de la semana.
nombresDias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# Programa principal:

diaSemana = int(input("Teclea el número del día de la semana (1 - 7): "))

diaSemana = diaSemana - 1 # Para ajustar la numeración a valores desde 0 a 6.
print(f"El día de la semana es {nombresDias[diaSemana]}")

