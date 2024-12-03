# archivo: operaciones.py
import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Realiza operaciones aritméticas entre dos números.")

# Definir los argumentos
parser.add_argument("num1", type=float, help="El primer número")
parser.add_argument("num2", type=float, help="El segundo número")
parser.add_argument(
    "-o", "--operacion",
    choices=["suma", "resta", "multiplicacion", "division"],
    default="suma",
    help="Operación a realizar: suma, resta, multiplicacion, division (por defecto: suma)"
)

# Parsear los argumentos
args = parser.parse_args()

# Realizar la operación
if args.operacion == "suma":
    resultado = args.num1 + args.num2
elif args.operacion == "resta":
    resultado = args.num1 - args.num2
elif args.operacion == "multiplicacion":
    resultado = args.num1 * args.num2
elif args.operacion == "division":
    if args.num2 == 0:
        print("Error: No se puede dividir entre cero.")
        exit()
    resultado = args.num1 / args.num2

# Mostrar el resultado
print(f"El resultado de la {args.operacion} es: {resultado}")
