import re

try:
    archivo = open("mbox-short.txt", mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

# Buscar las líneas en un archivo que contengan la palabra "From"
def buscar_sin_regexp(archivo):
    total = 0
    for linea in archivo:
        linea = linea.rstrip()
        if re.search("From", linea):
            print(linea)
            total += 1
    print("Total de coincidencias:", total)


def buscar_al_inicio(archivo):
    total = 0
    for linea in archivo:
        linea = linea.rstrip()
        #if re.search("^From:", linea): # Buscar al inicio de la línea
        #if re.search("^F..m:", linea): # "." cualquier caracter.
        if re.search("^From:.+@", linea):
            print(linea)
            total += 1
    print("Total de coincidencias:", total)


def buscar_todos(archivo):
    total = 0
    lista = []
    for linea in archivo:
        linea = linea.rstrip()
        # findall devuelve una lista con las coincidencias
        # cualquier palabra que no empiece con espacio en blanco
        # y siga de un arroba y de varios caracteres que no sean
        # espacio en blanco.
        lista = re.findall("[a-zA-Z0-9]\S*@\S*[a-zA-Z]", linea)
        if len(lista) > 0:
            print(lista)
            total += 1
    print("Total de coincidencias:", total)


# buscar_sin_regexp(archivo)
# buscar_al_inicio(archivo)
buscar_todos(archivo)