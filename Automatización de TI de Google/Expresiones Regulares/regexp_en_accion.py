import re

# Leer un archivo con una lista de todos los países.
with open("./Expresiones Regulares/paises.txt", encoding="utf-8") as archivo:
    paises = archivo.read()

# Buscar el país que empiece con las letras Ar y termine con na. Se utiliza
# el flag re.MULTILINE porque sino el ^ toma el inicio de la cadena y no el
# inicio de cada línea; lo mismo con el $.
print(re.search(r"^Ar.*na$", paises, re.MULTILINE))

# Patrón para validar el nombre de variables. Deben empezar por letras o guiones
# bajos y luego pueden tener cualquier cantidad de letras, números o guiones bajos.
# Nota: [a-zA-Z0-9_] = \w
patron = r"^[a-zA-Z_]\w*$"
print(re.search(patron, "_este_es_un_nombre_de_variable_valido"))
print(re.search(patron, "este no es un nombre de variable permitido"))
print(re.search(patron, "miVariable1"))
print(re.search(patron, "2mivariable"))

# Ejercicio:
# ***********

# Complete el código para verificar si el texto aprobado parece una oración
# estándar, lo que significa que comienza con una letra mayúscula, 
# seguida de al menos algunas letras minúsculas o un espacio, y termina con 
# un punto, un signo de interrogación o un signo de exclamación. 
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s].*[.?!]", text)
  return result != None

print("\nEjercicio: \n***********")
print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True