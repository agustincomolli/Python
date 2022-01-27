import json

numeros = [2,3,5,7,11,13]
nombre_archivo = "26-numeros.json"

# Escribir archivo.
with open(nombre_archivo, "w") as archivo:
    json.dump(numeros, archivo)

# Leer archivo.
with open(nombre_archivo, "r") as archivo:
    contenido = json.load(archivo)

print(contenido)


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


def saludar_usuario():
    """Saludar al usuario por su nombre."""
    nombre_usuario = obtener_usuario_guardado()
    if nombre_usuario:
        print(f"¡Bienvenido {nombre_usuario}!")
    else:
        nombre_usuario = obtener_nuevo_usuario()
        print(f"¡Te recordaré cuando vuelvas {nombre_usuario}!")


saludar_usuario()