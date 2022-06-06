#! python3

# Si una palabra comienza con una vocal, la palabra yay se agrega al final de 
# la misma. Si una palabra comienza con una consonante o grupo de consonantes 
# (como ch o gr ), esa consonante o grupo se mueve al final de la palabra 
# seguido de ay .


def obtener_prefijo_no_letras(palabra):
    """Separar los caracteres que no son letras del principio de la palabra."""

    prefijo_no_letras = ""
    while len(palabra) > 0 and not palabra[0].isalpha():
        prefijo_no_letras += palabra[0]
        palabra = palabra[1:]
    return palabra, prefijo_no_letras


def obtener_sufijo_no_letras(palabra):
    """Separar los caracteres que no son letras del final de la palabra."""

    sufijo_no_letras = ""
    while not palabra[-1].isalpha():
        sufijo_no_letras += palabra[-1]
        palabra = palabra[:-1]
    return palabra, sufijo_no_letras


def obtener_prefijo_consonantes(palabra):
    """Separar las consonantes del comienzo de la palabra."""

    prefijo_consonantes = ""
    vocales = ("a", "e", "i", "o", "u")
    while len(palabra) > 0 and not palabra[0] in vocales:
        prefijo_consonantes += palabra[0]
        palabra = palabra[1:]
    return palabra,prefijo_consonantes


def traducir(frase):
    lista_palabras = frase.split() # Dividir la frase en una lista de palabras.
    lista_traducida = []

    for palabra in lista_palabras:
        palabra, prefijo_no_letras = obtener_prefijo_no_letras(palabra)
    
        if len(palabra) == 0:
            lista_traducida.append(prefijo_no_letras)
            continue # Pasar a la siguiente palabra.

        palabra, sufijo_no_letras = obtener_sufijo_no_letras(palabra)

        # Recordar si la palabra estaba en mayúsculas o en título.
        era_mayus = palabra.isupper()
        era_titulo = palabra.istitle()

        # Poner en minúsuculas la palabra para la traducción.
        palabra = palabra.lower()

        palabra, prefijo_consonantes = obtener_prefijo_consonantes(palabra)

        # Agregar la terminación "ay" a la palabra.
        if prefijo_consonantes != "":
            palabra += prefijo_consonantes + "ay"
        else:
            palabra += "yay"

        # Volver a poner la palabra en mayúsculas o en título.
        if era_mayus:
            palabra = palabra.upper()
        elif era_titulo:
            palabra = palabra.title()

        # Agregar los caracteres que no son letras al principio o al final de la
        # palabra.
        lista_traducida.append(prefijo_no_letras + palabra + sufijo_no_letras)

    # Unir todas las palabras en una sola cadena.
    traduccion = " ".join(lista_traducida)
    return traduccion


frase = input("Ingrese una frase para traducir: ")
print(traducir(frase))

