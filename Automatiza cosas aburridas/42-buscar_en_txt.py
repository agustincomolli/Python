# Abrir todos los archivos txt en un directorio y buscar las líneas que
# coincidan con la expresión regular ingresada por el usuario.

import re
import os
from pathlib import Path

# Generar expresión regular.
texto_buscado = input("Buscar: ")
# Convertir en formato raw.
texto_buscado = fr"{texto_buscado}"
reg_exp = re.compile(texto_buscado)

# Cambiar el directorio actual.
ruta_archivos = Path("D:/Users/Agustín/Cursos/Python/" +
                "Automatiza cosas aburridas")
os.chdir(ruta_archivos)
print(f"Directorio actual:\n{Path.cwd()}")

# Obtener una lista de archivos txt.
archivos_txt = list(ruta_archivos.glob("*.txt"))

# Recorrer todos los archivos txt.
for archivo in archivos_txt:
    contenido = open(archivo,mode="r", encoding="UTF-8")
    # Recorrer el archivo por líneas.
    for linea in contenido:
        resultado = reg_exp.search(linea)
        if resultado != None:
            print(resultado)
    contenido.close()