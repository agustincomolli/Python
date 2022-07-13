from pathlib import Path

def ver_archivo(ruta_archivo:Path):
    """Imprime el contenido del archivo"""
    
    archivo = open(ruta_archivo, mode="r", encoding="UTF-8")
    print(archivo.read())
    archivo.close()


ruta_archivo = Path(Path.cwd() / "Automatiza cosas aburridas", "prueba.txt")

# Abrir archivo en modo escritura.
archivo = open(ruta_archivo, mode="w", encoding="UTF-8")
archivo.write("¡Hola mundo!")
archivo.close()

# Ver el contenido del archivo.
ver_archivo(ruta_archivo)

# Abrir archivo en modo append ("agregar")
archivo = open(ruta_archivo, mode="a", encoding="UTF-8")
archivo.write("\n-> Esto es una línea nueva.")
archivo.close()

# Ver el contenido del archivo.
print() # Para dejar un renglón en blanco.
ver_archivo(ruta_archivo)

