"""
Ejemplos de listas
"""

animals = ["gato", "murciélago", "rata", "elefante"]

print("Toda la lista:", animals)
print("El primer elemento:", animals[0])
print("El último elemento:", animals[len(animals) - 1])
print("El último elemento:", animals[- 1])
print("Una porción de la lista:", animals[1:3])
print("Hasta el 2° item de la lista:", animals[:2])
print("Después del 2° item en adelante:", animals[2:])
print("La lista tiene", len(animals), "items.")

# Modifica el 2° item.
animals[1] = "perro"
print("Lista modificada", animals)
birds = ["gorrión", "paloma", "gallina", "pato"]
# Concatena dos listas.
animals = animals + birds
print("Agregando una lista a la lista:", animals)
# Borra un item de la lista
del animals[-2] # La gallina
print("Borramos el item 'gallina' de la lista:", animals)
