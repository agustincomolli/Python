#!/usr/bin/env python3

import re
import sys

# Pasar como argumento la ubicación y el nombre de un archivo.
archivo = sys.argv[1]

# Crear un diccionario para guardar la cantidad de veces que aparecen los usuarios.
nombres_de_usuario = {}

# Abrir el archivo y recorrerlo línea a línea.
with open(archivo) as lector_archivo:
    for linea in lector_archivo:
        # Si la línea no contiene la palabra "CRON", continuar con la siguiente.
        if not "CRON" in linea:
            continue
        patron = r"USER \((\w+)\)$"
        filtrado = re.search(patron, linea)
        print(filtrado[1])
        # Generar un diccionario con los nombres de usuario y las veces que aparecen.
        if filtrado == None:
            continue
        nombre = filtrado[1]
        nombres_de_usuario[nombre] = nombres_de_usuario.get(nombre, 0) + 1

print(nombres_de_usuario)