nombre_archivo = input("Ingrese el nombre del archivo: ")
correos_por_dia = {}

try:
    archivo = open(nombre_archivo, mode="r")
except:
    print("ERROR. El archivo no está disponible.")
    quit()

for linea in archivo:
    palabras = linea.split()
    if (len(palabras) == 0) or (palabras[0] != "From"):
        continue
    correos_por_dia[palabras[2]] = correos_por_dia.get(palabras[2], 0) + 1

print(correos_por_dia)
archivo.close()