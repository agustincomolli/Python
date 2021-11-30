correos = {}

nombre_archivo = input("Ingrese el nombre del archivo: ")

try:
    archivo = open(nombre_archivo, mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

for linea in archivo:
    palabras = linea.split()
    if (len(palabras) == 0) or (palabras[0] != "From"):
        continue
    hora = palabras[5].split(":")
    correos[hora[0]] = correos.get(hora[0], 0) + 1

archivo.close()

lista = []
for hora, cantidad in list(correos.items()):
    lista.append((hora, cantidad))
lista.sort()
print("Correos por hora:\n" + ("=" * 17))
for hora, cantidad in lista:
    print(hora, cantidad)