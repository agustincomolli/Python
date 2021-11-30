# Abrir un archivo.
archivo = open("texto.txt")
# Leer una línea del archivo.
print(archivo.readline())
print(archivo.readline())
# Leer el resto del archivo.
print(archivo.read())
# Cerrar el archivo.
archivo.close()

# Con la instrucción with se abre un archivo y
# al finalizar se cierra el archivo de forma automática.
with open("texto.txt") as archivo:
    print(archivo.readline())

