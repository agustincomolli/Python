# Llamar a la función capitalize() mediante tres técnicas diferentes.
# La función capitalize() garantiza que el primer carácter de una 
# cadena esté en mayúscula. Solo se escribe en mayúscula la primera 
# letra de la cadena.
print("\nPaso 1: \n********")

mensaje = str.capitalize("primer mensaje")
print(mensaje)

mensaje = "segundo mensaje".capitalize()
print(mensaje)

mensaje = "tercer mensaje"
print(mensaje.capitalize())

# Llamar a funciones que modifican las mayúsculas y minúsculas de la cadena.
print("\nPaso 2: \n********")

mensaje = "¡hola mundo!"
print(mensaje.lower()) # Pasar a minúsculas.
print(mensaje.upper()) # Pasar a mayúsculas.

mensaje = mensaje.title() # Pasar a título.
print(mensaje)
print(mensaje.swapcase()) # Intercambiar mayúsculas y minúsculas.

# Contar el número de veces que una cadena se encuentra en otra.
print("\nPaso 3: \n********")

localizacion = "Mississipi"
print(localizacion.count("s"))
# Averiguar cuántos caracteres hay en una cadena.
print(len("¿Cuántos caracteres hay en esta cadena?"))

# Llama a las funciones que inspeccionan el contenido de la cadena.
print("\nPaso 4: \n********")

mensaje = "automovil"

print(mensaje.startswith("a"))
print(mensaje.startswith("u"))
print(mensaje.startswith("au"))

print(mensaje.endswith("l"))
print(mensaje.endswith("i"))
print(mensaje.endswith("il"))

# Encontrar la posición de una cadena dentro de otra cadena.
print("\nPaso 5: \n********")

mensaje = "El rápido zorro marrón salta sobre el perro perezoso."

print(mensaje.find("e"))
print(mensaje.find("z"))
print(mensaje.find("E"))

# Eliminar los caracteres vacíos de la izquierda, los de la derecha, o ambos.
print("\nPaso 6: \n********")

mensaje = "    medio    "
print("." + mensaje.lstrip() + ".")
print("." + mensaje.rstrip() + ".")
print("." + mensaje.strip() + ".")

# Reemplazar a una cadena encontrada en otra cadena.
print("\nPaso 7: \n********")

mensaje = "La brevedad es la esencia del ingenio."
mensaje = mensaje.replace("la esencia", "el alma")
print(mensaje)

# Justificar una cadena agregando caracteres de espacio vacío.
print("\nPaso 8: \n********")

mensaje = "hola"

print(mensaje.rjust(20))
print(mensaje.rjust(20, "-"))
print(mensaje.ljust(20))
print(mensaje.ljust(20, "-"))