# Escriba una función que tome una cadena y haga lo mismo que el método de 
# cadena strip() . Si no se pasan otros argumentos que no sean la cadena 
# que se va a eliminar, los espacios en blanco se eliminarán del principio 
# y del final de la cadena. De lo contrario, los caracteres especificados 
# en el segundo argumento de la función se eliminarán de la cadena.

import re

def strip_regexp(texto, cadena_borrar = " "):
    """Borra una cadena de caracteres del texto especificado."""
    texto = str(texto)
    cadena_borrar =str(cadena_borrar)
    regexp_borrar = re.compile(cadena_borrar)
    texto = regexp_borrar.sub(r"", texto)
    return texto


texto_prueba = " Hola que tal amigos, ¿cómo están? aeiou"
print(strip_regexp(texto_prueba))
print(strip_regexp(texto_prueba, "H"))
print(strip_regexp(texto_prueba, "a"))
print(strip_regexp(texto_prueba, "aeiou"))
print(strip_regexp(texto_prueba, "[¿?]"))