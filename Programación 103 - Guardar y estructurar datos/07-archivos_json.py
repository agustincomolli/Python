import json
from typing import Type

datos = {
    "Nombre": "Neil Amstrong",
    "Edad": 82,
    "Aficiones": ["Diseño de aviones", "Pesca", "Astronomía"]
}

# Escribir un archivo JSON.
with open("neil.json", mode="w", encoding="utf-8") as archivo:
    json.dump(datos, archivo)

# Leer un archivo JSON.
with open("neil.json", mode="r") as archivo:
    datos_archivo = json.load(archivo)

print(datos_archivo)