import csv

def leer_archivo():
    with open("comidas.csv") as archivo_csv:
        comidas = csv.reader(archivo_csv, delimiter=",")
        for fila in comidas:
            print(fila)

def escribir_archivo():
    nombre = "Agustin"
    comida = "Cordero"

    # newline = '' obliga a Python a no utilizar un carácter de 
    # "nueva línea" al insertar una nueva línea en el archivo.
    with open("comidas.csv", mode="a", newline="") as archivo_csv:
        comidas = csv.writer(archivo_csv, delimiter=",")
        comidas.writerow([nombre, comida])

escribir_archivo()
leer_archivo()
