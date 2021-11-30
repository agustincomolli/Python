# Comparar dos cadenas con comillas simples '' y dobles ""
print("\nPaso 1: \n********")
primera_cadena = 'Una cadena literal'
segunda_cadena = "Una cadena literal"

print(primera_cadena == segunda_cadena) # Puede usar comillas simples o dobles.

# Usar comillas dentro de otras comillas.
print("\nPaso 2: \n********")
tercer_cadena = 'Una cadena literal entre comillas simples con una " comilla doble.'
cuarta_cadena = "Una cadena literal entre comillas dobles con una ' comilla simple"

print(tercer_cadena)
print(cuarta_cadena)

# Usar secuencias de escape.
print("\nPaso 3: \n********")
quinta_cadena = 'Una sola cadena literal entre comillas con \' comillas simples escapadas'
sexta_cadena = "Una cadena literal entre comillas dobles con \" comillas dobles"
septima_cadena = 'Una cadena literal con un \n carácter de nueva línea'
octava_cadena = 'Una cadena literal con \tun carácter de tabulación'

print(quinta_cadena)
print(sexta_cadena)
print(septima_cadena)
print(octava_cadena)

# Agregar código que muestra cadenas sin formato.
print("\nPaso 4: \n********")

novena_cadena = r'Una cadena literal con un carácter \n de nueva línea impresa sin procesar'

print(novena_cadena)

# Agregar código que usa cadenas de varias líneas.
print("\nPaso 5: \n********")
decima_cadena = '''Una cadena literal
en más de una línea
a veces conocido como una cadena textual.\n'''
undecima_cadena = """Otra cadena literal
en más de una línea
usando comillas dobles."""

print(decima_cadena)
print(undecima_cadena)

# Dar formato a la cadena mediante la función print().
print("\nPaso 6: \n********")

primer_nombre = "Agustín"
segundo_nombre = "Alfredo"
apellido = "Comolli"

print(primer_nombre, segundo_nombre)
print(primer_nombre, segundo_nombre, apellido)
print(primer_nombre, segundo_nombre, apellido, sep="-")
print(primer_nombre, segundo_nombre, apellido, sep="-", end=".")