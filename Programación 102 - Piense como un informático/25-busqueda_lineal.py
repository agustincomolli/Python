from random import randint

# Buscar un número en una lista desordenada. Si el número
# no se encuentra devolver -1.
def buscar_linealmente(elemento, lista):
    encontrado = -1
    # Ordenar la lista.
    lista = sorted(lista)
    print(lista)
    # Recorrer la lista.
    for posicion, item in enumerate(lista,1):
        # Si el elemento es encontrado...
        if item == elemento:
            # Guardar la posición y dejar de recorrer la lista.
            encontrado = posicion
            break
    # Devolver la posición de elemento en la lista
    return encontrado

# Generar una lista de 20 números aleatorios.
lista_numeros = [randint(1, 100) for i in range(20)]

print(f"Lista de números:\n{lista_numeros}")
buscado = int(input("Ingrese el número a buscar: "))

encontrado = buscar_linealmente(buscado, lista_numeros)
if encontrado > -1:
    print(f"El número se encuentra en la posición {encontrado}.")
else:
    print("El número no se encuentra en la lista.")