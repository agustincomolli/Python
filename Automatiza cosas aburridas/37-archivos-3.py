import os
from pathlib import Path

# Ver el tamaño de un archivo.
print("Ver el tamaño de un archivo:")
print(f"calc.exe: {os.path.getsize('C:/Windows/System32/calc.exe')} bytes")

# Ver los archivos del directorio actual.
print("\nVer los archivos del directorio actual:")
print(os.listdir('.'))

# Ver el tamaño total de todos los archivos del directorio C:/Windows/System32.
tamaño_total = 0
for archivo in os.listdir("C:/Windows/System32"):
    tamaño_total += os.path.getsize(os.path.join("C:/Windows/System32", archivo))
print(f"\nTamaño total directorio C:/Windows/System32: {tamaño_total} bytes")

# Ver archivos usando patrones globales.
ruta = Path("D:/Users/Agustín/Documents")
lista_archivos = list(ruta.glob("*.txt"))
print(f"\nLista de archivos .txt en D:/Users/Agustín/Documents: {lista_archivos}")
lista_archivos = list(ruta.glob("N*.docx"))
print(f"\nLista de archivos N*.docx en D:/Users/Agustín/Documents: {lista_archivos}")