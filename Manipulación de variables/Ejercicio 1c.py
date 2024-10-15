#Programa para calcular la solución de la ecuación de 2º grado

a = 0 # Coeficiente de x^2 en la ecuación.
b = 0 # Coeficiente de x en la ecuación.
c = 0 # Término independiente de la ecuación.
x1 = 0 # Solución con "+" de la ecuación.
x2 = 0 # Solución con "-" de la ecuación.

a = float(input("Introduce el coeficiente de x^2: "))
b = float(input("Introduce el coeficiente de x: "))
c = float(input("Introduce el término independiente: "))
x1 = (-b+(b*b-4*a*c)**(1/2))/(2*a)
x2 = (-b-(b*b-4*a*c)**(1/2))/(2*a)

print("Las soluciones de la ecuación son: ", x1, " y ", x2)

