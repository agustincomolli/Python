from random import randint

# Buscar un número en una lista desordenada. Si el número
# no se encuentra devolver -1.
def buscar_binariamente(elemento, lista):
    encontrado = -1
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = int((izquierda + derecha) / 2)
        if lista[medio] > elemento:
            derecha = medio - 1
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            encontrado = medio + 1
            break
    # Devolver la posición de elemento en la lista
    return encontrado


# Generar una lista de 20 números aleatorios.
lista_numeros = [randint(1, 100) for i in range(20)]

print(f"Lista de números:\n{lista_numeros}")
# Ordenar la lista.
lista_numeros = sorted(lista_numeros)
print(f"\nLista ordenada: \n{lista_numeros}")

buscado = int(input("\nIngrese el número a buscar: "))

encontrado = buscar_binariamente(buscado, lista_numeros)
if encontrado > -1:
    print(f"El número se encuentra en la posición {encontrado}.")
else:
    print("El número no se encuentra en la lista.")