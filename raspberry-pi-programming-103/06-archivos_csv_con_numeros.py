import csv

# Leer datos del archivo.
def leer_archivo():
    with open("personas.csv", newline="") as archivo:
        personas = csv.reader(archivo, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
        for persona in personas:
            print(persona)
            print(type(persona[0]), type(persona[1]))

leer_archivo()