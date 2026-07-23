import re

try:
    archivo = open("mbox.txt", mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

patron_regexp = input("Ingrese una expresión regular: ")
resultado = []
total = 0

for linea in archivo:
    linea = linea.rstrip()
    resultado = re.findall(patron_regexp, linea)
    if len(resultado) > 0:
        total += 1

print("mbox.txt tiene", total, "líneas que coinciden con", patron_regexp)

archivo.close()