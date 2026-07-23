palabras_unicas = []
with open("romeo.txt", mode="r") as archivo:
    for linea in archivo:
        palabras = linea.split()
        for palabra in palabras:
            if palabra not in palabras_unicas:
                palabras_unicas.append(palabra)
palabras_unicas.sort()
print("Lista de palabras únicas:\n\n", palabras_unicas)