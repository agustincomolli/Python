"""
Agregando items a una lista.
"""

cats: list[str] = []
while True:
    print("Ingrese el nombre del", len(cats) + 1, "gato",
          "(O no ingrese nada para para el programa.)"
          )
    name = input("> ")

    if name == "":
        break

    cats += [name]

print("Los nombres de los gatos son: ")

for name in cats[:-1]:
    print(name, end=", ")

print(cats[-1])
