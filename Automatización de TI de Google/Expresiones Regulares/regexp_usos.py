import re

# Buscar el número de proceso usando el método index.
log = "July 31 07:51:48 mycompyter bad_process[12345]: ERROR Performing package upgrade"
indice = log.index("[")
print(log[indice + 1: indice + 6])

# Buscar el número de proceso usando expresiones regulares.
expresion_regular = r"\[(\d+)\]"
resultado = re.search(expresion_regular, log)
print(resultado[1])