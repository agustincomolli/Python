import re

text = """
1) En el vasto océano de datos, las expresiones regulares son como faros guía. 
Con Python, puedes buscar patrones en cadenas de texto de manera poderosa y 
flexible. 2) Usa el módulo 're' para encontrar coincidencias, validar formatos 
y extraer información. Desde correos electrónicos hasta números de teléfono, 
las expresiones regulares te permiten navegar por la maraña de información 
con precisión quirúrgica. 3) ¡Explora el mundo de las ER con Python y desbloquea 
un nuevo nivel de manipulación de datos!
"""

# Buscar la primer coincidencia con la palabra "Python".
result = re.search("Python", text)
print("Buscar la primer coincidencia con la palabra 'Python'")
print(result)

# Buscar todas las coincidencias con la palabra "Python"
result = re.findall("Python", text)
print("Buscar todas las coincidencias con la palabra 'Python'")
print(result)

# \d -> Busca dígitos [0-9]
result = re.findall(r"\d", text)
print("Busca dígitos [0-9]")
print(result)

# \D -> Busca todo lo que NO sea dígitos.
result = re.findall(r"\D", text)
print("Busca todo lo que NO sea dígitos")
print(result)

# \w -> Busca caracteres alfa numéricos [a-z A-Z 0-9 _]
result = re.findall(r"\w", text)
print("Busca caracteres alfa numéricos [a-z A-Z 0-9 _]")
print(result)

# \W -> Busca caracteres que NO sean alfa numéricos [a-z A-Z 0-9 _]
result = re.findall(r"\W", text)
print("Busca caracteres que NO sean alfa numéricos [a-z A-Z 0-9 _]")
print(result)

# \s -> Busca espacios en blanco [" ", \t, \n]
result = re.findall(r"\s", text)
print("Busca espacios en blanco [" ", \t, \n]")
print(result)

# \S -> Busca caracteres que NO sean espacios en blanco [" ", \t, \n]
result = re.findall(r"\S", text)
print(" Busca caracteres que NO sean espacios en blanco [" ", \t, \n]")
print(result)
