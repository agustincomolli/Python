"""
Juego de adivinar el número
"""

import random

print("Estoy pensando en un número del 1 al 20.")

secret_number = random.randint(1, 20)

# Pregunta al usuario 6 veces.
for guesses_taken in range(6):
    print("Adivina")
    guess = int(input("> "))
    guesses_taken = guesses_taken + 1
    if guess < secret_number:
        print("Tu número es es muy bajo")
    elif guess > secret_number:
        print("Tu número es muy alto.")
    else:
        break # Esta condición es la respuesta correcta!

if guess == secret_number:
    print("¡Buen trabajo! ¡Lo adivinaste en", str(guesses_taken + 1), "intentos.")
else:
    print("¡Noo, el número era:", secret_number)
