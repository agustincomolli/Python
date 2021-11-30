# Leer y cerrar archivos automáticamente.
with open("./un_archivo.txt", "r") as archivo:
    datos_archivo = archivo.read()

print(datos_archivo)
