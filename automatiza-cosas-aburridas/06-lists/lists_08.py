"""
Eliminación de un item en una lista y ordenamiento con métodos.
"""


def print_list(list_to_print):
    """
    Imprime en pantalla los items de una lista.

    Args:
        list_to_print (list): La lista para imprimir.
    """

    print(" - ", end="")
    for item in list_to_print:
        print(item, end=" ")

    print()


animals = ["perro", "gato", "rata", "paloma", "conejo", "gallina"]
# Ordena la lista
animals.sort()

print("Lista de animales original: ")
print_list(animals)

animal_to_remove = input("\n¿Qué animal desea quitar?: ")

try:
    # Elimina un item por su nombre.
    animals.remove(animal_to_remove)

    print("\nLista después de eliminar un item.")
    print_list(animals)
except ValueError:
    print("ERROR: El valor ingresado no está en la lista.")
