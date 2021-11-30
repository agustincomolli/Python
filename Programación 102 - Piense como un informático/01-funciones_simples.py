# Crear una lista de compras inicial.
lista_compras = ["Pan", "Leche", "Manzanas", "Chocolate", "Arroz integral", "Polenta"]

def mostrar_lista():
    print("\n*** Lista de compras ***")
    # Imprimir cada item de la lista, línea a línea.
    for item in lista_compras:
        print(item)

mostrar_lista()

# Agregar un item a la lista.
lista_compras.append("Azúcar")

mostrar_lista()
