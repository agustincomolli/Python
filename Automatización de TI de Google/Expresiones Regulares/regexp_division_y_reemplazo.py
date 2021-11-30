import re

# Dividir un texto en oraciones.
resultado = re.split(r"[.?!]", "Una oración. Otra oración más? La última oración!")
print(resultado)
# Si queremos incluir los elementos de división...
resultado = re.split(r"([.?!])", "Una oración. Otra oración más? La última oración!")
print(resultado)

# Reemplazar una cadena con expresiones regulares.
resultado = re.sub(r"[\w.%+-]+@[\w.]+", "[REDACTADO]", "Recibido un correo electrónico de agustincomolli@yahoo.com.ar")
print(resultado)

resultado = re.sub("^([\w.-]*), ([\w.-]*)$", r"\2 \1", "Comolli, Agustín")
print(resultado)

# Ejercicio:
# **********

# Queremos dividir un fragmento de texto por la palabra "a" o "el", 
# como se implementa en el siguiente código. ¿Cuál es la lista dividida resultante?

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))