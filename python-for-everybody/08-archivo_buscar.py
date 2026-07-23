print("SPAM Confidence\n" + "="* 15 + "\n")
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Huevo de pascua (Easter egg).
if nombre_archivo == "na na boo boo":
    print("¡Eso será tu madre! ^.-")
    quit()

try:
    archivo = open(nombre_archivo)
except:
    print("ERROR: El archivo no exite o no puede ser abierto.")
    quit()

total_lineas = 0
total_spam = 0
for linea in archivo:
    if linea.startswith("X-DSPAM-Confidence:"):
        posicion = linea.find(":")
        numero = linea[posicion + 1:]
        numero = numero.strip()
        numero = float(numero)
        total_lineas += 1
        total_spam += numero

print("Confianza promedio en spam:", total_spam / total_lineas, "\n")
