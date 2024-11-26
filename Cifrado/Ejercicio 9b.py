"""En este miniprograma vamos a aprender a descifrar un texto"""

from cryptography.fernet import Fernet

# Variables.
clave = "" # Contendrá la clave generada por Fernet.
frase = "" # Contendrá la frase sin cifrar.
fraseCifrada = "" # Contrendrá la frase ya cifrada.


# Funciones.


def load_key(): # Función que carga la clave desde el archivo en que se guardó.
    
    return open("./Cifrado/clave.key", "rb").read()


# Programa principal.

clave = load_key()
fraseCifrada = input("Teclea la frase cifrada: ")
f = Fernet(clave)
frase = f.decrypt(fraseCifrada)
frase = frase.decode() # Decodifico desde binario en UTF-8 a formato cadena (str).

print(frase)

