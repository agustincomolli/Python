cadena = input("Ingresa algo de texto: ")

def invertir_cadena(cadena_texto):
    cadena_invertida = ""
    for caracter in reversed(cadena_texto):
        cadena_invertida += caracter
    return cadena_invertida

print(invertir_cadena(cadena))