# Añadir contenido a un archivo existente.
nombre_archivo = "24-programando.txt"

with open(nombre_archivo, "a", encoding="UTF8") as archivo:
    archivo.write("\nTambién me encanta encontrar significado en grandes " + \
        "conjuntos de datos.\n")
    archivo.write("Me encanta crear aplicaciones que puedan ejecutarse en " + \
        "un navegador.")
