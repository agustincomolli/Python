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
