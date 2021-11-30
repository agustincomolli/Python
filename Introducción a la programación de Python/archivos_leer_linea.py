lineas_camelot = []

with open("./camelot.txt", "r") as archivo:
    for linea in archivo:
        lineas_camelot.append(linea.strip())

print(lineas_camelot)