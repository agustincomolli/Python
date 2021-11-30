import re

nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    archivo = open(nombre_archivo, mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

patron_regexp = "([0-9]+)"
resultado = []
suma = 0
total = 0

for linea in archivo:
    linea = linea.rstrip()
    resultado = re.findall(patron_regexp, linea)
    if len(resultado) > 0:
        for i in range(len(resultado)):
            total += 1
            suma += int(resultado[i])

print("Suma:", suma)
print("Coincidencias:", total)

archivo.close()