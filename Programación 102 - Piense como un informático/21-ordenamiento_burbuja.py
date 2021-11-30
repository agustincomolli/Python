from random import randint

# Ordenar una lista con el método de la burbuja.
def ordenar_burbuja(desordenada):
    # Crear copia de la lista para no modificar la original
    ordenada = desordenada[:]
    intercambiado = True

    # Mientras haya un intercambio de valores...
    while intercambiado:
        intercambiado = False
        # Iterar en la lista...
        for i in range(len(ordenada) - 1):
            if ordenada[i] > ordenada[i + 1]:
                # Intercambiar valores.
                ordenada[i], ordenada[i + 1] = ordenada[i + 1], ordenada[i]
                intercambiado = True
    
    return ordenada

lista_desordenada = [randint(0,9) for i in range(randint(5,20))]
print(f"Lista desordenada:\n{lista_desordenada}")
print(f"\nLista ordenada:\n{ordenar_burbuja(lista_desordenada)}")
