# Operaciones con variables integer o float.
print("\nOperaciones con variables".upper())
number = 1 + 1
print(f"Suma: {number}")
number = 3 - 2
print(f"Resta: {number}")
number += 3.5
print(f"Otra suma: {number}")

# Operaciones con strings.
# Concatenar:
text = "Hola" + " " + "Agustín"
text += ", ¿cómo estás?"
print(text)
# Multiplicar una cadena:
text = "hola "
text_2 = text * 3
print(text_2)

# Operadores de pertenencia (in, not in).
text = "Hola Agustín bienvenido a Python"
print("¿Está 'Agustín' en la variable 'text':", "Agustín" in text)
print("¿Está 'Lorena' en la variable 'text':", "Lorena" in text)
print("¿Agustín NO está estudiando Visual Basic?:", "Visual Basic" not in text)