"""
Todo lo que necesitas saber es que este programa simula un lanzamiento de moneda:

≈ 50% del tiempo, es "Cara".
≈ 50% del tiempo, es "Cruz".

"""
import random

num = random.randint(0, 1) # nos dará un número aleatorio entre 0 y 1

if num > 0.5:
    print("Cara 🪙")
else:
    print("Cruz 🪙")