import os
from pathlib import Path

directorio_inicial = Path("D:/Users/Agustín/Cursos/Python/Automatiza cosas "
                          + "aburridas")

# os.walk(ruta) recorre todos las carpetas, subcarpetas y archivos que hay en la 
# ruta.
for carpeta, subcarpetas, archivos in os.walk(directorio_inicial):
    print(f"Carpeta actual: {carpeta}")
    
    for subcarpeta in subcarpetas:
        print(f"Subcarpeta de {carpeta}: {subcarpeta}\n")
    
    for archivo in archivos:
        print(f"Archivo en {carpeta}: \t{archivo}")
    print()