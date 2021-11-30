# Recorrer en bucle
print("\nPaso 1: \n********")

import random

rodada = 0
cuenta = 0

while rodada != 5:
    cuenta = cuenta + 1
    rodada = random.randint(1,5)
    print(rodada)

print(f"Se necesitaron {cuenta} rodadas para llegar a 5.")

# Usar las instrucciones opcionales "break" y "else"
print("\nPaso 2: \n********")

import random

rodada = 0
cuenta = 0

print("La primera persona que llegue a 5 gana.")

while rodada != 5:
    nombre = input("Ingrese un nombre o \"q\" para salir: ")
    if nombre == "q":
        break

    cuenta = cuenta + 1
    rodada = random.randint(1,5)
    print(f"{nombre} ha sacado {rodada}")
else:
    print(f"*** ¡¡¡{nombre} ha ganado!!! ***".upper())

print(f"Has tirado el dado {cuenta} veces.")

# Controlar qué sucede cuando el usuario no introduce ningún valor.
print("\nPaso 3: \n********")

import random

rodada = 0
cuenta = 0

while rodada != 5:
    nombre = input("Ingrese un nombre o \"q\" para salir: ")

    if nombre.strip() == "": # ELiminar espacios vacíos y chequear.
        continue

    if nombre.strip() == "q":
        break

    cuenta = cuenta + 1
    rodada = random.randint(1,5)
    print(f"{nombre} ha sacado {rodada}")
else:
    print(f"*** ¡¡¡{nombre} ha ganado!!! ***".upper())

print(f"Has tirado el dado {cuenta} veces.")