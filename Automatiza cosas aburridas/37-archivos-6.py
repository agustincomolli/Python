from pathlib import Path

# Obtener la ruta del archivo.
ruta_archivo = Path(Path.cwd() / "Automatiza cosas aburridas", "soneto.txt")
print(f"Abriendo el archivo: '{ruta_archivo}'")

# Comprobar que el archivo exista.
if ruta_archivo.exists():
    # Abrir el archivo
    archivo = open(ruta_archivo, encoding="UTF-8")
    print("El archivo ha sido abierto con éxito.")
else:
    print("El archivo no existe.")
    exit()

# Leer el archivo.
contenido_archivo = archivo.read()
print(f"\nEl archivo contiene:\n{contenido_archivo}")

# Obtener una lista con las líneas del archivo.
archivo = open(ruta_archivo, encoding="UTF-8")
lista_lineas = archivo.readlines()
print(f"\nLista con las líneas del archivo:\n{lista_lineas}")