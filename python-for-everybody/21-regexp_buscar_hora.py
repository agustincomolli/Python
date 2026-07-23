# Busque líneas que comiencen con De y un carácter seguido de un número 
# de dos dígitos entre 00 y 99 seguido de ':'
# Luego imprima el número si es mayor que cero

import re

try:
    archivo = open("mbox-short.txt", mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

total = 0
regexp = "^From .* ([0-9][0-9]:\S+):"

for linea in archivo:
    linea.rstrip()
    resultado = re.findall(regexp, linea)
    if len(resultado) > 0:
        print(resultado[0])
        total += 1

print("Total de coincidencias:", total)
archivo.close()