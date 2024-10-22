"""Programa de Login que compruebe el usuario y contraseña en un diccionario predefinido. El usuario
tendrá máximo 3 intentos, y al acceder correctamente muestra un mensaje de bienvenida, con su
y apellidos."""

# Importación de librerías:

from os import system

# Declaración de variables:

usuarios = { # Diccionario con la "base de datos" de usarios de la web
		"aexposito":
		    {"nombre": "Antonio",
		    "apellidos": {"primerApellido": "Expósito", "segundoApellido": "Núñez"},
		    "password": "123456"},
	    "fgonzalez":
		    {"nombre": "Francisco",
		    "apellidos": {"primerApellido": "González", "segundoApellido": "Martínez"},
		    "password": "jejejaja"},
	    "lcastillo":
		    {"nombre": "Lourdes",
		    "apellidos": {"primerApellido": "Prieto", "segundoApellido": "Valverde"},
		    "password": "6789"}
	    }

numMaximoIntentos = 3 # El número máximo de intentos de acceso, antes de denegarlo.
numIntentos = 0 # Cuantifica el número de intentos fallidos en login.
usuario = "" # Pido por teclado el nombre de usuario.
contrasena = "" # Para pedir por teclado la contraseña.

# Programa principal:

system("cls")

while usuario not in usuarios.keys() and numIntentos < numMaximoIntentos: # Mientras que el usuario no esté y el número de intentos sea aceptable.
    usuario = input("Introduce tu usuario: ")
    if usuario in usuarios.keys(): # Pido la contraseña sólo si el usuario está en el diccionario.
        contrasena = input("Contraseña: ")
        if contrasena != usuarios[usuario]["password"]: # si la contraseña no está en el diccionario.
            usuario = "" # Para evitar que salga del bucle, aunque sea erróna la contraseña.
            numIntentos += 1 # Aumento el número de intentos.
            print(f"La contraseña que has escrito es incorrecta. Te quedan {numMaximoIntentos-numIntentos} intentos.")
    else:
        numIntentos += 1
        print(f"Usuario no encontrado. Te quedan {numMaximoIntentos-numIntentos} intentos.")

if numIntentos == numMaximoIntentos: # Ha salido del bucle porque ha superado el número de intentos.
    print("Has superado el número máximo de intentos. Usuario bloqueado.")
else: # Ha salido del bucle cuando las credenciales son correctas.
    print(f"Acceso concedido. Bienvenid@ {usuarios[usuario]["nombre"]} {usuarios[usuario]["apellidos"]["primerApellido"]} {usuarios[usuario]["apellidos"]["segundoApellido"]}.")
