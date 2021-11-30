import re

try:
    archivo = open("mbox-short.txt", mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

# Busque líneas que comiencen con 'X' seguida de cualquier carácter 
# que no sea un espacio en blanco y ':' seguido de un espacio y cualquier 
# número. El número puede incluir un decimal.
def buscar(archivo):
    total = 0
    for linea in archivo:
        linea = linea.rstrip()
        if re.search("^X\S*: [0-9.]+", linea):
            print(linea)
            total += 1
    return total


# Busque líneas que comiencen con 'X' seguida de cualquier carácter 
# que no sea un espacio en blanco y ':' seguido de un espacio y cualquier 
# número. El número puede incluir un decimal. Luego imprima el número.
def buscar_numeros(archivo):
    total = 0
    regexp = "^X\S*: ([0-9.]+)"
    lista_numeros = []
    for linea in archivo:
        linea = linea.rstrip()
        lista_numeros = re.findall(regexp, linea)
        if len(lista_numeros) > 0:
            print(lista_numeros)
            total += 1
    return total


# Busque líneas que comiencen con 'Detalles: rev =' seguido de números.
# Luego imprima el número si encuentra uno.
def buscar_otros(archivo):
    total = 0
    regexp = "^Details:.*rev=([0-9]+)"
    resultado = []
    for linea in archivo:
        linea = linea.rstrip()
        lista_numeros = re.findall(regexp, linea)
        if len(lista_numeros) > 0:
            print(lista_numeros)
            total += 1
    return total


print("Total de coincidencias:", buscar_otros(archivo))
archivo.close()