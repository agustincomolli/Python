def contar_palabras(archivo):
    """Cuenta las palabras que hay en un archivo."""
    nombre_archivo = archivo

    try:
        with open(nombre_archivo, "r", encoding="UTF8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"Lo siento, el archivo {nombre_archivo} no existe.")
    else:
        # Contar las palabras del archivo.
        palabras = contenido.split()
        print(f"El archivo '{nombre_archivo}' tiene {len(palabras)} palabras.")


libros = ["25-alice.txt", "25-siddhartha.txt", "25-moby_dick.txt", "25-little_women.txt"]
for libro in libros:
    contar_palabras(libro)