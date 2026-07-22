"""
Agregando items a la lista con los métodos append.
"""

names = ["agustín", "lorena", "carlitos", "marcela",
         "adrián", "gustavo", "laura", "ariel"]

name_to_search = input("Escriba un nombre a buscar: ")

try:
    print("Ese nombre está en el índice", str(
        names.index(name_to_search.lower())))
except ValueError:
    print("Ese nombre no está en la lista.")
    answer = input("¿Desea agregarlo? [y|n]: ")
    if answer == "y":
        names.append(name_to_search.lower())
        print("Se agregó", name_to_search, "a la lista:")
        print(names)
