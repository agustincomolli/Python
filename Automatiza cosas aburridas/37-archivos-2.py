import os
from pathlib import Path

# Cambiar el directorio actual.
print(f"Directorio actual: {Path.cwd()}")
os.chdir("C:")
print(f"Nuevo directorio: {Path.cwd()}")
os.chdir(Path("D:/Users/Agustín/Cursos/Python/Automatiza cosas aburridas"))
print(f"Directorio del curso: {Path.cwd()}")

# Crear un directorio si no existe ya.
if Path.exists(Path("./nueva carpeta")) != True:
    os.mkdir("./nueva carpeta")
    print("Se ha creado el directorio 'nueva carpeta'.")

# Determinar si una ruta es relativa o absoluta.
print(f"'D:/Users/Agustín' es una ruta absoluta: {Path('D:/Users/Agustín').is_absolute()}")
print(f"'./nueva carpeta' es una ruta absoluta: {Path('./nueva carpeta').is_absolute()}")

# Extraer los atributos de la ruta de un archivo.
archivo = Path.cwd() / "37-archivos-2.py"
print(f"Anchor: {archivo.anchor}")
print(f"Padre: {archivo.parent}")
print(f"Nombre: {archivo.name}")
print(f"Extensión: {archivo.suffix}")
