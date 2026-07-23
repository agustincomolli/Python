# 10-11. Número favorito: escriba un programa que solicite el número favorito 
# del usuario. Use json.dump() para almacenar este número en un archivo. 
# Escriba un programa separado que lea este valor e imprima el mensaje, “¡Sé 
# su número favorito! Su _____."

# 10-12. Número favorito recordado: combine los dos programas del ejercicio 
# 10-11 en un solo archivo. Si el número ya está almacenado, informe el 
# número favorito al usuario. De lo contrario, solicite el número favorito 
# del usuario y guárdelo en un archivo. Ejecute el programa dos veces para 
# ver si funciona.

# 10-13. Verificar usuario: la lista final de Remember_me.py asume que el 
# usuario ya ingresó su nombre de usuario o que el programa se está 
# ejecutando por primera vez. Deberíamos modificarlo en caso de que el 
# usuario actual no sea la última persona que usó el programa.
# Antes de imprimir un mensaje de bienvenida en greeting_user(), pregunte 
# al usuario si este es el nombre de usuario correcto. Si no es así, llame a 
# get_new_username() para obtener el nombre de usuario correcto.

import json
from tkinter.tix import Tree

# print("Ejercicio 10-11\n" + "*" * 15)

# try:
#     numero = int(input("Ingrese su número favorito: "))
# except ValueError:
#     print("Debe ingresar un valor numérico.")
# else:
#     nombre_archivo = "26-numero_favorito.json"
#     with open(nombre_archivo, "w") as archivo:
#         json.dump(numero, archivo)

# try:
#     with open(nombre_archivo, "r") as archivo:
#         contenido = json.load(archivo)
#         print(f"Sé su número favorito, es el {contenido}.")
# except FileNotFoundError:
#     print("Archivo no encontrado.")


print("\nEjercicio 10-11 y 10-12\n" + "*" * 23)

def obtener_numero_guardado():
    """Obtener el número favorito del usuario si está disponible."""
    nombre_archivo = "26-numero_favorito.json"
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = json.load(archivo)
    except FileNotFoundError:
        return None
    else:
        return contenido


def obtener_nuevo_numero():
    """Solicita el número favorito del usuario para guardarlo."""
    try:
        numero = int(input("Ingrese su número favorito: "))
    except ValueError:
        print("Debe ingresar un valor numérico.")
    else:
        nombre_archivo = "26-numero_favorito.json"
        with open(nombre_archivo, "w") as archivo:
            json.dump(numero, archivo)


numero_favorito = obtener_numero_guardado()
if numero_favorito:
    print(f"Sé su número favorito, es el {numero_favorito}.")
else:
    obtener_nuevo_numero()


print("Ejercicio 10-13\n" + "*" * 15)
# Cargar el nombre de usuario si fue guardado previamente.
# En caso contrario preguntar el nombre de usuario y guardarlo.
def obtener_usuario_guardado():
    """Obtener el nombre de usuario si está disponible."""
    nombre_archivo = "26-usuario.json"
    try:
        with open(nombre_archivo,"r", encoding="utf8") as archivo:
            usuario = json.load(archivo)
    except FileNotFoundError:
        return None
    else:
        return usuario


def obtener_nuevo_usuario():
    """Pregunta por un nuevo usuario."""
    nombre_archivo = "26-usuario.json"
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    with open(nombre_archivo, "w", encoding="utf8") as archivo:
        json.dump(nombre_usuario, archivo)
    return nombre_usuario


def chequear_usuario_actual(usuario):
    """Pregunta si el usuario actual es el último usuario que utilizó el 
    sistema."""
    while True:
        respuesta = input(f"¿'{usuario}', este es su " + \
            "usuario? [s|n]: ").lower()
        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False


def saludar_usuario():
    """Saludar al usuario por su nombre."""
    nombre_usuario = obtener_usuario_guardado()
    if nombre_usuario:
        if chequear_usuario_actual(nombre_usuario):
            print(f"¡Bienvenido {nombre_usuario}!")
        else:
            nombre_usuario = obtener_nuevo_usuario()
            print(f"¡Te recordaré cuando vuelvas {nombre_usuario}!")
    else:
        nombre_usuario = obtener_nuevo_usuario()
        print(f"¡Te recordaré cuando vuelvas {nombre_usuario}!")


saludar_usuario()