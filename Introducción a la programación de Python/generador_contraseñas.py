# TODO: Primero importe el módulo `random`
import random

# Comenzamos con una `lista_de_palabras` vacía
archivo_de_palabras = "palabras.txt"
lista_de_palabras = []

# Rellenamos la lista_de_palabras del archivo `palabras.txt`
with open(archivo_de_palabras, 'r') as palabras:
    for linea in palabras:
        # eliminar los espacios en blanco y poner todo en minúsculas
        palabra = linea.strip().lower()
        # no incluya palabras que sean demasiado largas o demasiado cortas
        if 3 < len(palabra) < 8:
            lista_de_palabras.append(palabra)


# TODO: Agregue su función generar_password a continuación
# Debería devolver una cadena que consta de tres palabras
# aleatorias concatenadas juntas sin espacios
def generar_password():
    password = ""
    for palabra in range(3):
        password += lista_de_palabras[random.randrange(len(lista_de_palabras))]
    return password


# Ahora probamos la función
print(generar_password())
