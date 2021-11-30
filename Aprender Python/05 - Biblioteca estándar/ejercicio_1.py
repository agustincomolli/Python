# Importar el módulo random.
print("\nPaso 1: \n********")

import random

valor = random.randint(1, 10)

print(f"Sacaste {valor}")

# Importar el módulo random y usar un alias.
print("\nPaso 2: \n********")

import random as dado

valor = dado.randint(1, 10)
print(f"Sacaste {valor}")