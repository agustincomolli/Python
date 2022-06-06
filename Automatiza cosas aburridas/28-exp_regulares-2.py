import re

# Poner expresiones entre paréntesis generará grupos.
re_numero_telefono = re.compile(r"\d{3}-\d{3}-\d{4}")

texto = '¿Es 415-555-4242 un número de teléfono?'
resultado = re_numero_telefono.search(texto)
print(texto)
if not resultado == None:
    print(f"Sí es un número de teléfono: {resultado.group()}")
else:
    print("Eso no es un número de teléfono.")

texto = '\n¿Moshi moshi es un número de teléfono?'
resultado = re_numero_telefono.search(texto)
print(texto)
if not resultado == None:
    print(f"Sí es un número de teléfono: {resultado.group()}")
else:
    print("Eso no es un número de teléfono.")

# Poner expresiones entre paréntesis generará grupos.
re_numero_telefono = re.compile(r"(\d{3})-(\d{3}-\d{4})")
texto = "\nMi número de teléfono es 415-555-4242"
resultado = re_numero_telefono.search(texto)
print(texto)
print(f"Código de área: {resultado.group(1)}")
print(f"Número de teléfono: {resultado.group(2)}")

# Poner "\(" o "\)" para mostrar los paréntesis en un texto.
re_numero_telefono = re.compile(r"(\(\d{3}\)) (\d{3}-\d{4})")
texto = "\nMi número de teléfono es (415) 555-4242"
resultado = re_numero_telefono.search(texto)
print(texto)
print(f"Código de área: {resultado.group(1)}")
print(f"Número de teléfono: {resultado.group(2)}")

# Poner "()?" es un grupo opcional.
re_numero_telefono = re.compile(r"(\d{3})?(\d{3}-\d{4})")
texto = "\nMi número de teléfono es 555-4242"
resultado = re_numero_telefono.search(texto)
print(texto)
print(f"Número de teléfono: {resultado.group()}")