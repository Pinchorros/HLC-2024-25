# Definición de funciones:

def agregarProducto(inventario):
    nombre = input("¿Qué producto quieres añadir al inventario? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        print(f"El producto '{nombre}' ya está dentro del inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        try:
            precio = float(input("Precio del artículo: "))
            cantidad = int(input("Cantidad de artículos: "))
        except ValueError:
            print(f"Error: El valor introducido no es numérico. Artículo {nombre} no añadido.")
        else:
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
            print(f"El producto '{nombre}' ha sido añadido a la lista.")
        
        print("")
        input("Pulsa una tecla para continuar...")


def listadoProductos(inventario):
    print("Listado de los elementos...")
    for nombre, valor in inventario.items(): # Recorro todo el diccionario principal.
        print(f"Producto: {nombre}, Precio: {valor["precio"]}, Cantidad: {valor["cantidad"]}.")

    print("")
    input("Pulsa una tecla para continuar...")     


def buscarProducto(inventario):
    nombre = input("¿Qué producto quieres buscar? ")
    nombre = nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        precio = inventario[nombre]["precio"]
        cantidad = inventario[nombre]["cantidad"]
        print(f"Producto: {nombre}, Precio: {precio}, Cantidad stock: {cantidad}")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
    print("")
    input("Pulsa una tecla para continuar...")



def actualizarCantidad(inventario):
    nombre = input("¿De qué producto quieres modificar el stock? ")
    nombre =  nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre not in inventario:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
        print("")
        input("Pulsa una tecla para continuar...")
    else:
        try:
            cantidad = int(input("Introduce la nueva cantidad en stock: "))
        except ValueError:
            print(f"La cantidad introducida no es numérica. No se puede actualizar el artículo {nombre}.")
        else:
            inventario[nombre]["cantidad"] = cantidad
            print(f"El producto '{nombre}' ha actualizado correctamente su stock a {cantidad} unidades.")
        print("")
        input("Pulsa una tecla para continuar...")



def eliminarProducto(inventario):
    nombre = input("¿Qué producto quieres eliminar? ")
    nombre = nombre.capitalize() # Para evitar duplicados por mayúsculas.
    if nombre in inventario:
        if inventario[nombre]["cantidad"] == 0:
            del inventario[nombre]
            print(f"El producto '{nombre}' ha sido eliminado del inventario.")
        else:
            print(f"No se puede eliminar el producto '{nombre}' ya que su stock no es 0.")
    else:
        print(f"El producto '{nombre}' no se encuentra en el inventario.")
    print("")
    input("Pulsa una tecla para continuar...")

