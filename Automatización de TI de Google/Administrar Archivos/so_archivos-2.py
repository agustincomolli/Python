import os, datetime

# Averiguar el tamaño de un archivo.
print("El tamaño del archivo \"texto.txt\" es de:", os.path.getsize("texto.txt"), "bytes.")

# Mostrar la fecha de modificación.
timestamp = os.path.getmtime("texto.txt")
fecha = datetime.datetime.fromtimestamp(timestamp)
print("El archivo fue modificado el:", fecha)