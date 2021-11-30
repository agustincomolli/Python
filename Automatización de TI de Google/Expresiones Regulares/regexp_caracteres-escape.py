import re

# Buscar .com en este caso da un resultado erróneo porque no toma el
# en la búsqueda.
print(re.search(r".com", "welcome"))

# En este caso el resultado es None porque se tomo la búsqueda ".com"
# correctamente.
print(re.search(r"\.com", "welcome"))

# Buscar usando \w* incluirá letras, números y guiones bajo.
print(re.search(r"\w*", "Esto es un ejemplo."))
print(re.search(r"\w*", "Esto_es_otro_ejemplo"))

# Ejercicio
#***********

# Complete el código para verificar si el texto pasado tiene al menos
# 2 grupos de caracteres alfanuméricos (incluidas letras, números y 
# guiones bajos) separados por uno o más caracteres de espacio en blanco.
import re
def check_character_groups(text):
  result = re.search(r"\w\s* \w*", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False