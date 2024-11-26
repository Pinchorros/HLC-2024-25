"""En este miniprograma vamos a aprender a descifrar el contenido de un archivo"""

from cryptography.fernet import Fernet

# Variables.
clave = "" # Contendrá la clave generada por Fernet.
nombreArchivo = "" # Contendrá el nombre del archivo a cifrar.


# Funciones.

def load_key(): # Función que carga la clave desde el archivo en que se guardó.
    
    return open("./Cifrado/clave.key", "rb").read()

def descifrar(nombreArchivo, clave):
    """
    Dado un nombre de archivo y clave, descifra el archivo y lo graba sin la extensión ".cifrado", si la tuviera
    """
    f = Fernet(clave)
    with open(nombreArchivo, "rb") as archivo: # Lee los datos del archivo cifrado
        datosCifrados = archivo.read()
    datos = f.decrypt(datosCifrados) # Descifra los datos
    if ".cifrado" in nombreArchivo: # Miro si el archivo original tiene la extensión ".cifrado"
        nombreArchivo = nombreArchivo.split('.')[:-1] # Elimino ".cifrado" (devuelve una lista)
        nombreArchivo = ".".join(nombreArchivo) # Uno la lista en una cadena, con "." en medio.
    with open(nombreArchivo, "wb") as archivo: # Escribe los datos en el archivo.
        archivo.write(datos)


# Programa principal.

clave = load_key() # Cargamos la clave de cifrado, desde el archivo "clave.key"
nombreArchivo = input("Teclea el nombre del archivo a descifrar: ")
nombreArchivo = "./Cifrado/" + nombreArchivo # Añado la ruta relativa del archivo.
descifrar(nombreArchivo, clave) # Cifro el archivo y lo guardo con el mismo nombre, pero extensión ".cifrado"

print(f"El archivo {nombreArchivo} ha sido descifrado correctamente.")


