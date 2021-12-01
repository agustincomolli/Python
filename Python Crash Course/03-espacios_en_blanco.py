# Espacios en blanco: 
# "\n" línea nueva
# "\t" tabulación.
mensaje = "Lenguajes de Programación:\n\t- Python,\n\t- Visual Basic,\n\t- Clipper"
print(mensaje)

# Eliminar espacios en blanco.
lenguaje_favorito = " Python "
print("'" + lenguaje_favorito + "'")
print("'" + lenguaje_favorito.rstrip() + "'") # a la derecha.
print("'" + lenguaje_favorito.lstrip() + "'") # a la izquiera.
print("'" + lenguaje_favorito.strip() + "'") # a ambos lados.

# Apóstrofes.
mensaje = 'San Agustín dijo: \n \
    \t\t"Nada conquista excepto la verdad, y la victoria de la verdad es el amor."'
print(mensaje)