# Buscar los dominios de los correos electrónicos 
# que aparezcan en el archivo solamente de las líneas que 
# comiencen con "From".
import re

try:
    archivo = open("mbox-short.txt", mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

patron_regexp = "^From .*@([^ ]*)"
total = 0
hosts = []

for linea in archivo:
    linea = linea.rstrip()
    hosts = re.findall(patron_regexp, linea)
    if len(hosts) > 0:
        print(hosts[0])
        total += 1

print("\nTotal de coincidencias:", total)
archivo.close()