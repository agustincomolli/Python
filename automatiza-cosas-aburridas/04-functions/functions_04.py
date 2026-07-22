"""
Funciones pasando los parámetros por su nombre.
"""

import random

print("Tirando la moneda... 🪙")
# Tira 20 veces una moneda.
for i in range(20):
    if random.randint(0, 1) == 0:
        print("😀", end=" ")
    else:
        print("❌", end=" ")

# Agrega una línea nueva al terminar.
print()
