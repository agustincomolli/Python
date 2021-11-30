import os

# Averiguar cuál es el directorio actual.
print("1 - El directorio actual es: \n -->", os.getcwd())

# Crear un nuevo directorio en la ubicación actual.
if not os.path.exists("Nueva Carpeta"):
    os.mkdir("Nueva Carpeta")
    print("2 - Se ha creado un nuevo directorio \"Nueva Carpeta\" en la ubicación actual.")

# Cambiar de directorio.
os.chdir("Nueva Carpeta")
print("3 - El directorio actual es: \n -->", os.getcwd())

# Eliminar directorio.
os.chdir("..")
os.rmdir("Nueva Carpeta")
print("4 - El directorio \"Nueva Carpeta\" ha sido eliminado. \n La ubicación actual es: \n -->", os.getcwd())

# Listar el contenido de un directorio.
print(os.listdir(".."))

# Identificar si el contenido de un directorio es un archivo o directorio.
directorio = ".."
for nombre in os.listdir(directorio):
    nombreCompleto = os.path.join(directorio, nombre)
    if os.path.isdir(nombreCompleto):
        print("{} es un directorio".format(nombreCompleto))
    else:
        print("{} es un archivo".format(nombreCompleto))