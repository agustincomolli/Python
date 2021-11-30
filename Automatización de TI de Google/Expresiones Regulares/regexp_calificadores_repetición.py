import re

# Buscar 5 letras en una palabra
print(re.search(r"[a-zA-Z]{5}", "dos gatos"))
# Buscar todos los resultados.
print(re.findall(r"[a-zA-Z]{5}", "En la reunión fuimos cinco gatos locos."))
# Buscar sólo palabras completas de 5 letras.
print(re.findall(r"\b[a-zA-Z]{5}\b", "En la reunión fuimos cinco gatos locos."))
# Buscar palabras que tengan entra 5 y 10 letras o números.
print(re.findall(r"\w{5,10}", "En la reunión fuimos cinco gatos locos."))
# Buscar una palabra que empiece con r y tenga entre 0 y 7 caracteres.
print(re.search(r"r\w{,7}", "En la reunión retornamos los cinco gatos locos."))

# Ejercicio:
# ***********

# La función long_words devuelve todas las palabras que tienen al menos 7 
# caracteres. Complete la expresión regular para completar esta función.

import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []