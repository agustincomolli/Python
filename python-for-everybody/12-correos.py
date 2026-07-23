contador = 0
try:
    with open("mbox-short.txt") as archivo:
        for linea in archivo:
            palabras = linea.split()
            if len(palabras) == 0 or (palabras[0] != "From"):
                continue
            print(palabras[1])
            contador += 1
except:
    print("ERROR: archivo no disponible.")

print(f"Había {contador} líneas en el archivo con From como la primera palabra")