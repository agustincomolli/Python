import os
import shutil
import zipfile
from pathlib import Path

carpeta_inicial = Path("D:/Users/Agustín/Cursos/Python/Automatiza cosas "
                          + "aburridas")
os.chdir(carpeta_inicial)

# Obtener el archivo zip.
ejemplo_zip = zipfile.ZipFile(carpeta_inicial / "ejemplo.zip")

# Mostrar el contenido del archivo.
print("Archivos que están dentro de ejemplo.zip:")
print(ejemplo_zip.namelist())

# Obtener la información de un archivo que está dentro del zip.
info_archivo = ejemplo_zip.getinfo("ejemplo/09-desafio.js")
print(f"\nTamaño del archivo \"09-desafio.js\": {info_archivo.file_size} bytes.")
print(f"Tamaño que ocupa comprimido: {info_archivo.compress_size} bytes.")
print("El archivo comprimido es " + 
      f"{round(info_archivo.file_size / info_archivo.compress_size, 2)} " 
      +"veces más pequeño que el archivo original.")

# Extraer todo el contenido del archvio zip.
ejemplo_zip.extractall()
print("\nSe han extraído todos los archivos.")

# Extraer un solo archivo del zip en una carpeta específica.
ejemplo_zip.extract("ejemplo/09-desafio.html", carpeta_inicial / "43-carpeta")
print("Se ha extraído el archivo 'ejemplo/09-desafio.html'.")

# Cerrar el archivo zip.
ejemplo_zip.close()

# Crear un archivo zip.
nuevo_archivo_zip = zipfile.ZipFile("nuevo_archivo.zip", mode="w")
nuevo_archivo_zip.write(carpeta_inicial / "soneto.txt", 
                        compress_type=zipfile.ZIP_DEFLATED)
nuevo_archivo_zip.close()
print("\nSe ha creado un nuevo archivo zip.")

# Eliminar la carpeta extraída y todos sus archivos.
input("Presione una ENTER para borrar todos los archivos y salir.")
shutil.rmtree(carpeta_inicial / "ejemplo")
shutil.rmtree(carpeta_inicial / "43-carpeta/ejemplo")
os.remove(carpeta_inicial / "nuevo_archivo.zip")
