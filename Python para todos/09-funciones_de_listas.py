lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def chop(lista):
    lista.remove(lista[0])
    lista.remove(lista[-1])
    return None


def middle(lista):
    copia_lista = lista[:]
    copia_lista.remove(copia_lista[0])
    copia_lista.remove(copia_lista[-1])
    return copia_lista


print("Lista original:", lista)
lista_nueva = middle(lista)
chop(lista)
print("Lista chop():", lista)
print("Lista middle():", lista_nueva)