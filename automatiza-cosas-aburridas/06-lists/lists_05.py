"""
Encontrando valores en una lista usando métodos.
"""

names = ["agustín", "lorena", "carlitos", "marcela",
         "adrián", "gustavo", "Laura", "ariel"]

name_to_search = input("Escriba un nombre a buscar: ")

try:
    print("Ese nombre está en el índice", str(
        names.index(name_to_search.lower())))
except ValueError:
    print("Ese nombre no está en la lista.")
