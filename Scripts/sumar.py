import sys

if len(sys.argv) < 3: # Recuerda que el primer parámetro es el nombre del programa
    print("Error: te faltan parámetros. Uso: python sumar.py num1 num2")
else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(f"La suma de {num1} + {num2} es {num1 + num2}")
