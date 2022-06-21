import os
from pathlib import Path

# Trabajando con archivos.
ruta_archivo = Path(Path.cwd()/ "Automatiza cosas aburridas", "prueba.txt")
if ruta_archivo.exists():
    print("El archivo existe")
else:
    ruta_archivo.write_text("¡Hola, mundo!\n\nEsto es una prueba.")
    print("El archivo se ha creado")

# Leer el archivo.
print("\nContenido del archivo:")
print(ruta_archivo.read_text())
