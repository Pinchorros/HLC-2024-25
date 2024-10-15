# Programa que muestra en pantalla la sunma de los N primeros números pares (se pedirá por teclado).

# Declaración de variables:
suma = 0 # Variable que acumula la suma de los números.
i = 0 # Variable índice con el que recorro el bucle.
numeroFinal = 0 # Valor final que indica cuando acaba el bucle (se pide por teclado)

numeroFinal = int(input("¿Cuántos valores quieres sumar? "))

for i in range(0, numeroFinal*2, 2):
    print("Número par:", end= " ")
    print(i)
    suma = suma + i

print("La suma total es:", suma)
