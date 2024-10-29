

def mediaPonderada(valor1, valor2, peso1 = 50, peso2 = 50):
    """Formato de la función: mediaPonderada(valor1, valor2, [peso1], [peso2]).
    En caso de no incluir los pesos, se calculará la media aritmética"""

    resultado = (valor1*peso1+valor2*peso2)/100 # Resultado es variable local.
    return resultado

resultado = 5 # Resultado es variable global

print(f"La media ponderada es {mediaPonderada(5, 8, 60, 40)}")

print(f"La media aritmética es {mediaPonderada(5, 8)}")

print(5*mediaPonderada(9, 5))

print(resultado)

