import pprint

# Contar cuántas veces aparecen las letras en la variable mensaje.
mensaje = "Era un día brillante y frío de abril, y los relojes daban " + \
    "las trece."

cuenta = {}

for letra in mensaje:
    cuenta.setdefault(letra, 0)
    cuenta[letra] += 1

pprint.pprint(cuenta)