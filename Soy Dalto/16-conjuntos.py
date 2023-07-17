# Crear un conjunto con la función set().
set_1 = set(["Dato 1"])
print(f"Primer conjunto: {set_1}")

# Unir dos conjuntos.
set_2 = {"Dato 2", "Dato 3"}
set_3 = {frozenset(set_2), "Dato 4"}
print(f"Conjuntos unidos: {set_3}")

# Teoría de conjuntos.
set_4 = {1,2,3,4,5,6}
set_5 = {1,3,5}

if set_5.issubset(set_4):
    print(f"El conjunto set_5 es un subconjunto de set_4")

if set_4.issuperset(set_5):
    print(f"El conjuto set_4 es un superconjunto de set_5")