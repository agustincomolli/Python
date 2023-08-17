import re

text = """
1) En el vasto océano de datos, las expresiones regulares son como faros guía. 
Con Python, puedes buscar patrones en cadenas de texto de manera poderosa y 
flexible. 
2) Usa el módulo 're' para encontrar coincidencias, validar formatos 
y extraer información. Desde correos electrónicos hasta números de teléfono, 
las expresiones regulares te permiten navegar por la maraña de información
con precisión quirúrgica. 3) ¡Explora el mundo de las ER con Python y desbloquea 
un nuevo nivel de manipulación de datos! 1234
"""

# Buscar la primer coincidencia con la palabra "Python".
result = re.search("Python", text)
print("Buscar la primer coincidencia con la palabra 'Python'")
print(result)

# Buscar todas las coincidencias con la palabra "Python"
result = re.findall("Python", text)
print("\nBuscar todas las coincidencias con la palabra 'Python'")
print(result)

# \d -> Busca dígitos [0-9]
result = re.findall(r"\d", text)
print("\nBusca dígitos [0-9]")
print(result)

# \D -> Busca todo lo que NO sea dígitos.
result = re.findall(r"\D", text)
print("\nBusca todo lo que NO sea dígitos")
print(result)

# \w -> Busca caracteres alfa numéricos [a-z A-Z 0-9 _]
result = re.findall(r"\w", text)
print("\nBusca caracteres alfa numéricos [a-z A-Z 0-9 _]")
print(result)

# \W -> Busca caracteres que NO sean alfa numéricos [a-z A-Z 0-9 _]
result = re.findall(r"\W", text)
print("\nBusca caracteres que NO sean alfa numéricos [a-z A-Z 0-9 _]")
print(result)

# \s -> Busca espacios en blanco [" ", \t, \n]
result = re.findall(r"\s", text)
print("\nBusca espacios en blanco [' ', \\t, \\n]")
print(result)

# \S -> Busca caracteres que NO sean espacios en blanco [" ", \t, \n]
result = re.findall(r"\S", text)
print("\nBusca caracteres que NO sean espacios en blanco [' ', \\t, \\n]")
print(result)

# \n -> Buscar saltos de línea [\n]
result = re.findall(r"\n", text)
print("\nBuscar saltos de línea [\\n]")
print(result)

# . -> Buscar todos los caracteres que NO sean saltos de línea [\n]
result = re.findall(r".", text)
print("\nBuscar todos los caracteres que NO sean saltos de línea [\\n]")
print(result)

# \{caracter} -> Buscar caracteres específicos que NO sean alfanuméricos
result = re.findall(r"\.", text)
print("\nBuscar caracteres específicos que NO sean alfanuméricos")
print(result)

# Buscar una cadena que busque un número seguido de un ) y un espacio en blanco
result = re.findall(r"\d\)\s", text)
print("\nBuscar una cadena que busque un número seguido de un ) y un " +
      "espacio en blanco")
print(result)

# ^ Buscar un número al principio de una línea
# flags=re.M activa la búsqueda multilínea.
result = re.findall(r"^\d", text, flags=re.M)
print("\nBuscar el principio de una línea")
print(result)

# $ Buscar una palabra al final de una línea
# flags=re.M activa la búsqueda multilínea.
result = re.findall(r"información$", text, flags=re.M)
print("\nBuscar una palabra al final de una línea")
print(result)

# {n} Buscar n cantidad de veces el valor de la izquierda
result = re.findall(r"\d{4}", text, flags=re.M)
print("\nBuscar 4 dígitos juntos")
print(result)

# {min,max} Buscar un valor en un rango.
result = re.findall(r"\d{1,4}", text, flags=re.M)
print("\nBuscar un dígito o como máximo 4 dígitos juntos")
print(result)

#() Buscar un conjunto de caracteres
result = re.findall(r"(ue)", text)
print("\nBuscar un conjunto de caracteres")
print(result)

# | Buscar una cosa o la otra
result = re.findall(r"\d|datos", text)
print("\nBuscar un dígito o la palabra datos")
print(result)