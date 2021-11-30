import re

def arreglar_nombre(nombre):
    resultado = re.search(r"^([\w \.-]*), ([\w \.-]*)$", nombre, re.MULTILINE)
    if resultado is None:
        return nombre
    return "{} {}".format(resultado[2], resultado[1])
