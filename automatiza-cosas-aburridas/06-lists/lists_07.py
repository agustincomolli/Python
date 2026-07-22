"""
Agregando items en un lugar determinado de la lista.
"""


def list_names(list_of_names):
    """
    Imprime el contenido de una lista de nombres con su índice.
    
    Args:
        list_of_names (list): Lista de nombres.
    """
    for i, name in enumerate(list_of_names):
        if i != len(list_of_names) - 1:
            print(i, "-", name.capitalize(), end=", ")
        else:
            print(i, "-", name.capitalize())


names = ["agustín", "lorena", "carlitos", "marcela",
         "adrián", "gustavo", "laura", "ariel"]

list_names(names)

while True:
    try:
        new_place = int(
            input("¿En qué lugar quieres agregar el nuevo nombre: "))
        break
    except ValueError:
        print("Debes ingresar un número entero.")

new_name = input("Escribe el nuevo nombre: ")
names.insert(new_place, new_name)

list_names(names)
