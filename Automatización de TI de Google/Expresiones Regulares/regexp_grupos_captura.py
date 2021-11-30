import re

with open("./Expresiones Regulares/nombres.txt") as archivo:
    lista_nombres = archivo.read()

# Buscar "apellidos, nombres" en lista_nombres.
# En las expresiones regulares los paréntesis generan grupos de coincidencia.
resultado = re.search(r"^([\w \.-]*), ([\w \.-]*)$", lista_nombres, re.MULTILINE)
# Devuelve una tupla con los grupos de expresiones regulares.
print(resultado.groups())
# El índice 0 devuelve la coincidencia completa.
print(resultado[0])
# El índice 1 devuelve el primer elemento del grupo.
print(resultado[1])
print(resultado[2])
print("{} {}".format(resultado[2], resultado[1]))

def arreglar_nombre(nombre):
    resultado = re.search(r"^([\w \.-]*), ([\w \.-]*)$", nombre, re.MULTILINE)
    if resultado is None:
        return nombre
    return "{} {}".format(resultado[2], resultado[1])

print(arreglar_nombre("Comolli, Agustín A."))
print(arreglar_nombre("Mellado Comolli, Lorena"))