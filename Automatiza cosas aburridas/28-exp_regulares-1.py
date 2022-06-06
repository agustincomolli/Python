# Verificar un patrón de texto SIN el uso de expresiones regulares.

def es_numero_telefono(texto):
    """Verificar si un número de teléfono coincide con el formato de EEUU."""

    if len(texto) != 12:
        return False
    
    for i in range(0,3):
        if not texto[i].isdecimal():
            return False

    if not texto[3] == "-":
        return False

    for i in range(4, 7):
        if not texto[i].isdecimal():
            return False
    
    if not texto[7] == "-":
        return False

    for i in range(8, 12):
        if not texto[i].isdecimal():
            return False

    return True


print('¿Es 415-555-4242 un número de teléfono?')
print(es_numero_telefono('415-555-4242'))
print('¿Moshi moshi es un número de teléfono?')
print(es_numero_telefono('Moshi moshi'))

mensaje = 'Llámame al 415-555-1011 mañana. 415-555-9999 es mi oficina.'
for i in range(len(mensaje)):
  fragmento = mensaje[i:i+12]
  if es_numero_telefono(fragmento):
        print('Número de teléfono encontrado: ' + fragmento)
print('Terminado')