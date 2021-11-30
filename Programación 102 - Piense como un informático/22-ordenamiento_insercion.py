from random import randint

# Ordenar una lista con el método de inserción.
def ordenar_insercion(lista_desordenada):
    lista = lista_desordenada[:]    # Copiar la lista original
    
    # Recorrer la lista empezando por el 2° elemento.
    for i in range(1, len(lista)):
        clave = lista[i]    # Extraer el elemento actual de la lista.
        marcador = i - 1    # Indice del elemento anterior al actual.

        # Mientras que el valor del elemento anterior (marcador) sea mayor
        # al valor de la de elemento actual y el indice de 
        # dicho elemento sea >= 0...
        while (lista[marcador] > clave) and (marcador >= 0):
            lista[marcador + 1] = lista[marcador]
            marcador -= 1

        lista[marcador + 1] = clave
    
    return lista # Devolver la lista ordenada.

desordenada = [randint(1, 20) for i in range(randint(5,20))]

print(f"Lista desordenada:\n {desordenada}\n")

print(f"Lista ordenada:\n {ordenar_insercion(desordenada)}")