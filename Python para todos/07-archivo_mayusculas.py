print("Lector de archivos\n" + "=" * 18 + "\n")
nombre_archivo = input("Ingrese el nombre del archivo: ")
try:
    # Abrir archivo.
    archivo = open(nombre_archivo, mode="r", encoding="UTF-8")
except:
    print("ERROR: No se puede abrir el archivo.")
    quit()
# Recorrer el archivo.
for linea in archivo:
    # Mostrar las líneas en mayúsculas.
    print(linea.upper().rstrip())
# Cerrar archivo.
archivo.close()