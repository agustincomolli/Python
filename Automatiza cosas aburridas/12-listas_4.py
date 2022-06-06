lista_compras = []
salir = False

def agregar_item():
    """Agregar un item a la lista."""
    print()
    item = input("Agregar: ")
    lista_compras.append(item.lower())
    print()


def modificar_item():
    """Modificar un item de la lista."""
    print()
    item = input("Ingrese el item a modificar: ")
    try:
        indice = lista_compras.index(item.lower())
        nuevo_valor = input("Ingrese el nuevo valor: ")
        lista_compras[indice] = nuevo_valor
    except ValueError:
        print(f"{item} no está en la lista.")
    print()


def eliminar_item():
    """Eliminar un item de la lista."""
    print()
    item = input("Ingrese el item a modificar: ")
    try:
        indice = lista_compras.index(item.lower())
        lista_compras.remove(item)
    except ValueError:
        print(f"{item} no está en la lista.")
    print()


while not salir:
    print("Lista de compras\n")
    print("1 - Agregar item.")
    print("2 - Modificar item.")
    print("3 - Eliminar item.")
    print("4 - Mostrar la lista.")
    print("5 - Salir.")

    menu = int(input("\nIngrese opción: "))
    if menu == 1:
        agregar_item()
    elif menu == 2:
        modificar_item()
    elif menu == 3:
        eliminar_item()
    elif menu == 4:
        # Ordenar lista y mostrarla.
        lista_compras.sort()
        print(f"\nLista de compras: {lista_compras}\n")
    elif menu == 5:
        salir = True