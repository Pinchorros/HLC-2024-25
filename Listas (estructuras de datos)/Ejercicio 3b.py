"""(Uso de listas) Pedirá por teclado la lista de los
números de la lotería de los últimos 7 días. Posteriormente
los mostrará ordenados de menor a mayor y de mayor a menor."""

# Declaración de variables:

numerosLoteria = [0, 0, 0, 0, 0, 0, 0]

for contador in range(0,7):
    numerosLoteria[contador] = int(input(f"Introduce el día de la lotería del {contador+1}º día: "))

numerosLoteria.sort() # Ordenar la lista de menor a mayor.

print(f"La lista ordenada de menor a mayor es: {numerosLoteria}")

numerosLoteria.sort(reverse = True) # Ordenar la lista de mayor a menor.

print(f"La lista ordenada de mayor a menor es: {numerosLoteria}")

