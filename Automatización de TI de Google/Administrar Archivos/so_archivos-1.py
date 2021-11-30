import os

# os.path.exists verifica si existe el archivo.
if os.path.exists("archivo_creado.txt"):
    # Eliminar un archivo.
    os.remove("archivo_creado.txt")
    print("Archivo \"archivo_creado.txt\" ELIMINADO")
else:
    print("El archivo no existe. ¡Vamos a crearlo!")
    # Crear el archivo.
    with open("archivo_para_renombrar.txt", "w") as archivo:
        archivo.write("El nombre original del archivo era \"archivo_para_renombrar.txt\"")
    # Renombrar el archivo.
    os.rename("archivo_para_renombrar.txt", "archivo_creado.txt")
