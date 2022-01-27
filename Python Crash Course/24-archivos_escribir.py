# Crear un archivo de múltiples líneas.
nombre_archivo = "24-programando.txt"

with open(nombre_archivo, "w", encoding="UTF8") as archivo:
    archivo.write("Me encanta la programación.\n")
    archivo.write("Me encanta crear nuevos juegos.")
