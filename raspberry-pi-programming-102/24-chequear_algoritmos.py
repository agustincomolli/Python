from random import randint
from time import time

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

def fusion(lista_a, lista_b):
    lista_ordenada = []
    # Mientras las listas contengan algún valor...
    while len(lista_a) > 0 and len(lista_b) > 0:
        # Si una valor es más chico que otro,
        # agregarlo a la lista ordenada y borrarlo
        # de la lista de origen.
        if lista_a[0] < lista_b[0]:
            lista_ordenada.append(lista_a.pop(0))
        else:
            lista_ordenada.append(lista_b.pop(0))
    
    # Si la lista a no tiene elementos:
    if len(lista_a) < 1:
        # Agregar a la lista ordenada todos los elementos
        # restantes de la lista b.
        lista_ordenada += lista_b
    else:
        lista_ordenada += lista_a

    return lista_ordenada

# Ordenar una lista según el método de fusión.
def ordenar_fusion(lista_desordenada):
    # Si la lista tiene 1 o 0 elementos se la considera
    # ordenada.
    if len(lista_desordenada) <= 1:
        return lista_desordenada
    else:
        # Buscar el medio de la lista y redondearlo.
        medio = int(len(lista_desordenada) / 2)
        # Dividir la lista en dos y volver a llamar a la función
        # recursiva para dividir la lista hasta que quede un
        # elemento.
        lista_izq = ordenar_fusion(lista_desordenada[:medio])
        lista_der = ordenar_fusion(lista_desordenada[medio:])
    return fusion(lista_izq, lista_der)

# Generar una lista de 1000 items con valores aleatorios.
lista_desordenada = [randint(0,100000) for i in range(1000)]
# Capturar la hora actual, antes de que el algoritmo se ejecute.
hora_inicio = time()
# Ejecutar el algoritmo de fusión.
ordenar_fusion(lista_desordenada)
# Calcular el tiempo del algoritmo restando la hora actual con la hora 
# de inicio.
tiempo_total = time() - hora_inicio
print(f"El algoritmo de fusión tomó {tiempo_total} segundos")

#Repetir el proceso con el algoritmo de inserción.
hora_inicio = time()
ordenar_insercion(lista_desordenada)
tiempo_total = time() - hora_inicio
print(f"El algoritmo de inserción tomó {tiempo_total} segundos")

#Repetir el proceso con el algoritmo de burbuja.
hora_inicio = time()
ordenar_burbuja(lista_desordenada)
tiempo_total = time() - hora_inicio
print(f"El algoritmo de burbuja tomó {tiempo_total} segundos")

#Repetir el proceso con el algoritmo de sorted().
hora_inicio = time()
sorted(lista_desordenada)
tiempo_total = time() - hora_inicio
print(f"La función sorted() tomó {tiempo_total} segundos")
