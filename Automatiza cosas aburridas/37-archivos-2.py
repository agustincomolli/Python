import os
from pathlib import Path

# Cambiar el directorio actual.
print(f"Directorio actual: {Path.cwd()}")
os.chdir("C:")
print(f"Nuevo directorio: {Path.cwd()}")
os.chdir(Path("D:/Users/Agustín/Cursos/Python/Automatiza cosas aburridas"))
print(f"Directorio del curso: {Path.cwd()}")
# Crear un directorio.
os.mkdir("./nueva carpeta")
