# Métodos.
print("Buscar elemento en la lista:")
lista_compras = ["yerba", "azúcar", "arroz", "fideos", "detergente"]
print(lista_compras)
elemento = input("Buscar: ")
try:
    # El método index devuelve el índice de un elemento de la lista.
    # Si no se encuentra el elemento genera un ValueError.
    indice = lista_compras.index(elemento)
    print(f"{elemento.capitalize()} se encuentra en la posición {indice}")
except ValueError:
    print(f"'{elemento.capitalize()}' no está en la lista.")
    respuesta = input("¿Desea agregarlo? [s|n]: ")
    if respuesta.lower() == "s":
        # Agregar item a la lista.
        lista_compras.append(elemento)
        print(lista_compras)