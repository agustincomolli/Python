def process_numbers(lista):
    
    lista_de_numeros = []

    # Si el parámetro no es una lista...
    if not isinstance(lista, list):
        return lista_de_numeros # Devolver una lista vacía.
    
    for item in lista:
        if isinstance(item, int) or isinstance(item, float):
            lista_de_numeros.append(item)
        elif isinstance(item, str) and item.isnumeric():
            lista_de_numeros.append(int(item))
    
    lista_de_numeros.sort()

    return lista_de_numeros

def process_names(lista):
    
    lista_de_nombres = []

    # Si el parámetro no es una lista...
    if not isinstance(lista, list):
        return lista_de_nombres # Devolver una lista vacía.

    for item in lista:
        if isinstance(item, str) and not item.isnumeric():
            lista_de_nombres.append(item)
    
    lista_de_nombres.sort()

    return lista_de_nombres