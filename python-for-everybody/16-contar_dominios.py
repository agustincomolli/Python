nombre_archivo = input("Ingrese el nombre del archivo: ")
dominios = {}
dominio = ""

try:
    archivo = open(nombre_archivo, mode="r")
except:
    print("ERROR: El archivo no está disponible.")
    quit()

for linea in archivo:
    palabras = linea.split()
    if (len(palabras) == 0) or (palabras[0] != "From"):
        continue
    dominio = palabras[1].split("@")
    dominios[dominio[1]] = dominios.get(dominio[1], 0) + 1

print(dominios)