"""
Juego de piedra, papel o tijeras contra la computadora.
"""

import random
import sys

wins = 0
looses = 0
ties = 0
computer_choice = ""

print("*** Piedra 🪨 , Papel 🧻 o Tijeras ✂️  ***")

while True:
    print(str(wins), "Ganadas,", str(looses), "Perdidas,", str(ties), "Empatadas")

    # Valida la entrada del usuario.
    while True:
        print("Escribe tu elección: pied(r)a, (p)apel, (t)ijeras, (s)alir")
        user_choice = input("> ")

        if user_choice == "s":
            sys.exit()
        elif user_choice in ("r", "p", "t"):
            break

        print("Escribe 'r', 'p', 't' o 's'")

    if user_choice == "r":
        print("🪨  PIEDRA versus ...")
    elif user_choice == "p":
        print("🧻  PAPEL versus ...")
    else:
        print("✂️  TIJERAS versus ...")

    # Obtiene la elección de la computadora.
    computer_choice_number = random.randint(1, 3)
    if computer_choice_number == 1:
        computer_choice = "r"
        print("🪨  PIEDRA")
    elif computer_choice_number == 2:
        computer_choice = "p"
        print("🧻  PAPEL")
    else:
        computer_choice = "t"
        print("✂️  TIJERAS")

    if user_choice == computer_choice:
        ties = ties + 1
        print("¡Es un empate!")
    elif user_choice == "r" and computer_choice == "t" or \
        user_choice == "p" and computer_choice == "r" or \
        user_choice == "t" and computer_choice == "p":
        wins = wins + 1
        print("¡Tu ganas 🥳!")
    else:
        looses = looses + 1
        print("Has perdido 🥲")
