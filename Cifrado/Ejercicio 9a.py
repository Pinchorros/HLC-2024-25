"""En este miniprograma vamos a aprender a cifrar un texto"""

from cryptography.fernet import Fernet

# Variables.
clave = "" # Contendrá la clave generada por Fernet.
frase = "" # Contendrá la frase sin cifrar.
fraseCifrada = "" # Contrendrá la frase ya cifrada.


# Funciones.

def write_key(): # Función que genera una clave y la guarda en un archivo
    
    clave = Fernet.generate_key()
    with open("./Cifrado/clave.key", "wb") as key_file:
        key_file.write(clave)

def load_key(): # Función que carga la clave desde el archivo en que se guardó.
    
    return open("./Cifrado/clave.key", "rb").read()


# Programa principal.

write_key() # Se debe ejecutar tan sólo la primera vez para generar la clave y guardarla en un archivo.
clave = load_key()
frase = input("Teclea la frase a cifrar: ")
frase = frase.encode() # Codifico desde formato cadena (str) a binario en UTF-8.
f = Fernet(clave)
fraseCifrada = f.encrypt(frase)

print(fraseCifrada)

