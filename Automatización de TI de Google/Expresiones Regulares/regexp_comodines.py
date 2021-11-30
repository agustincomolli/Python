import re

# Buscar la palabra python tanto que empiece en mayúsculas como en minúsculas.
print(re.search(r"[Pp]ython", "Python"))
# Buscar la palabra que comience con un caracter alfabético en minúscula.
print(re.search(r"[a-z]era", "El final de la carretera"))
print(re.search(r"[a-z]era", "Cuando era invierno"))
# Buscar la palabra que incluya caracteres alfanumérico en mayúsculas y minúsculas.
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
# Buscar un caracter que no sea una letra dentro de la frase.
print(re.search(r"[^a-zA-Z]", "Esta es una oración con espacios."))
# Buscar una palabra u otra en la frase.
print(re.search(r"gato|perro", "Me gustan mucho los perros pero no tanto los gatos."))
# Buscar ambas expresiones a la vez de la frase anterior.
print(re.findall(r"gato|perro", "Me gustan mucho los perros pero no tanto los gatos."))

def check_punctuation (text):
  result = re.search(r"[,.;:'!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False