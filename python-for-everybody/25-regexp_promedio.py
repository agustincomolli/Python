import re

nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    archivo = open(nombre_archivo, mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

patron_regexp = "^N.*: ([0-9]+)"
resultado = []
total = 0
suma = 0

for linea in archivo:
    linea = linea.rstrip()
    resultado = re.findall(patron_regexp, linea)
    if len(resultado) > 0:
        total += 1
        suma += int(resultado[0])

print("El promedio es:", int(suma / total))

archivo.close()