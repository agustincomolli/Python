text = "Hola, buenos días. Esta es una cadena de texto."

# Texto en mayúsculas.
result = text.upper()
print(f"Mayúsculas:\n{result}")

# Texto en minúsuclas.
result = text.lower()
print(f"\nMinúsculas:\n{result}")

# Mayúscula sólo en la primera palabra.
result = text.capitalize()
print(f"\nTipo oración:\n{result}")

# Buscar una cadena dentro de otra.
position = text.find("día")
print(f"\nLa palabra 'día' está en la posición {position}")