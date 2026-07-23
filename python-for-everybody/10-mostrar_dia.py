try:
    with open("mbox-short.txt", mode="r") as archivo:
        for linea in archivo:
            palabras = linea.split()
            if (len(palabras) == 0) or (palabras[0] != "From"):
                continue
            print(palabras[2])
except:
    print("ERROR: El archivo no está disponible.")