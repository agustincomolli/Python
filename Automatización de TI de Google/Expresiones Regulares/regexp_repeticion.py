import re

# Buscar la cadena que contenga "Py" seguido de cualquier númer de
# caracteres hasta que encuentre la última letra "n".
print(re.search(r"Py.*n", "Pygmaleon"))

# El siguiene ejemplo toma las dos palabras porque empieza con "Py" seguido
# de cualquier cantidad de caracteres hasta encontrar la última letra "n".
print(re.search(r"Py.*n", "Python Programming"))

# Aquí toma la primer palabra porque busca solamente una palabra que empieza
# con Py seguido de cualquier cantidad de caracters alfabéticos por eso los 
# espacios no se cuentan.
print(re.search(r"Py[a-z]*n", "Pygmaleon Python Programming"))

print(re.search(r"Py[a-z]*n", "Pyn"))

# El signo + busca una o varias coincidencias del caracter anterior.
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))

# El signo ? busca una o ninguna coincidencia con el caracter anterior.
print(re.search(r"p?each", "to each their own."))
print(re.search(r"p?each", "I like peaches."))

# Ejercicio:
#************

# La función repeating_letter_a comprueba si el texto pasado incluye la
# letra "a" (minúscula o mayúscula) al menos dos veces. Por ejemplo, 
# repetating_letter_a ("banana") es True, mientras que 
# repeating_letter_a ("piña") es False. Complete el código para que 
# esto funcione.
def repeating_letter_a(text):
  result = re.search(r"[Aa].*a.*", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True