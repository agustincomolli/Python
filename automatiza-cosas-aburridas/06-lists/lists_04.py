"""
Usando enumerate para trabajar con los índices y los elementos de la lista.
"""

supplies = ["lápices", "gomas de borrar", "agendas", "reglas", "bolígrafos"]

for i, product in enumerate(supplies):
    print("El índice", str(i), "en suministros corresponde a:", product)
