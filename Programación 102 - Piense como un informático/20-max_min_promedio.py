from random import randint

# Obtener el valor máximo de una lista.
def obtener_maximo(lista):
    maximo = 0

    for item in lista:
        if item > maximo:
            maximo = item

    return maximo

# Obtener el valor mínimo de una lista.
def obtener_minimo(lista):
    minimo = 99
    
    for item in lista:
        if item < minimo:
            minimo = item

    return minimo

# Obtener el promedio de una lista.
def obtener_promedio(lista):
    promedio = 0
    suma = 0

    for item in lista:
        suma += item

    promedio = suma / len(lista)
    return promedio

calificaciones = [randint(1, 10) for i in range(10)]

print("Lista de calificacioneses", calificaciones)
print("Valor máximo:", obtener_maximo(calificaciones))
print("Valor mínimo:", obtener_minimo(calificaciones))
print("Valor promedio:", obtener_promedio(calificaciones))

