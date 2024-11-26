"""En este miniprograma vamos a aprender a cifrar el contenido de un archivo"""

from cryptography.fernet import Fernet

# Variables.
clave = "" # Contendrá la clave generada por Fernet.
nombreArchivo = "" # Contendrá el nombre del archivo a cifrar.


# Funciones.

def write_key(): # Función que genera una clave y la guarda en un archivo
    
    clave = Fernet.generate_key()
    with open("./Cifrado/clave.key", "wb") as key_file:
        key_file.write(clave)

def load_key(): # Función que carga la clave desde el archivo en que se guardó.
    
    return open("./Cifrado/clave.key", "rb").read()

def cifrar(nombreArchivo, clave): 
    """Función que dado el nombreArchivo y la clave, cifra el archivo y lo guarda en disco con extensión .cifrado."""
    f = Fernet(clave) # Inicializamos el objeto "Fernet"
    with open(nombreArchivo, "rb") as archivo: # Leemos el contenido del archivo.
        datosArchivo = archivo.read()
    datosCifrados = f.encrypt(datosArchivo) # Ciframos el contenido del archivo.
    with open(nombreArchivo + ".cifrado", "wb") as archivo:
        archivo.write(datosCifrados) # Guardamos en disco el archivo, pero con datos cifrados (sobreescribo los datos originales)


# Programa principal.

clave = load_key() # Cargamos la clave de cifrado, desde el archivo "clave.key"
nombreArchivo = input("Teclea el nombre del archivo a cifrar: ")
nombreArchivo = "./Cifrado/" + nombreArchivo # Añado la ruta relativa del archivo.
cifrar(nombreArchivo, clave) # Cifro el archivo y lo guardo con el mismo nombre, pero extensión ".cifrado"

print(f"El archivo {nombreArchivo} ha sido cifrado correctamente ->{nombreArchivo}.cifrado")


