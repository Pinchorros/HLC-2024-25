# Programa que suma los primeros 50 números impares (y muestra la suma por pantalla).

# Declaración de variables:
suma = 0 # Inicializo a cero, la variable donde guardo la suma.
numero = 0 # Variable numérica para recorrer los números.

for numero in range(1,101, 2):
    suma = suma + numero

print("La suma total es: ", suma)


