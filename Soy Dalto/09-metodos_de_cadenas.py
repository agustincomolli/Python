text = "Hola, buenos días. Esta es una cadena de texto."

# Texto en mayúsculas.
result = text.upper()
print(f"- Mayúsculas:\n  {result}")

# Texto en minúsuclas.
result = text.lower()
print(f"- Minúsculas:\n  {result}")

# Mayúscula sólo en la primera palabra.
result = text.capitalize()
print(f"- Tipo oración:\n  {result}")

# Buscar una cadena dentro de otra. Sino se encuentra devuelve -1.
position = text.find("día")
print(f"\nLa palabra 'día' está en la posición {position}")
position = text.find("Agustín")
print(f"La palabra 'Agustín' está en la posición {position}")

# Comprobar si la cadena de texto es un número.
age = "46"
alpha = "textosinespacios"
print(f"\n¿La variable 'age' es un número? {age.isnumeric()}")
print(f"¿La variable 'age' tiene solo letras? {age.isalpha()}")
print(f"¿La variable 'text' tiene solo letras? {text.isalpha()}")
print(f"¿La variable 'alpha' tiene solo letras? {alpha.isalpha()}")

# Contar cuantas veces aparece una cadena dentro de otra. Si no se encuentra
# devuelve 0.
count = text.count("a")
print(f"\nLa letra 'a' aparece {count} veces.")

# Contar cuantos caracteres tiene una cadena.
print(f"La variable 'text' tiene {len(text)} caracteres")

# Comprobar si una cadena empieza o termina de una forma determinada.
text_start = text.startswith("Hola")
print(f"\n¿La variable 'text' empieza con la palabra 'Hola'? {text_start}")
text_ends = text.endswith("zaraza")
print(f"¿La variable 'text' termina con la palabra 'zaraza'? {text_ends}")

# Reemplazar una subcadena por otra, dentro de una cadena.
replaced = text.replace("buenos días", "maestro")
print(f"\nLa cadena reemplazada queda así:\n{replaced}")

# Crear una lista con las palabras separadas por espacios.
print(f"\nLista de palabras:\n{text.split()}")