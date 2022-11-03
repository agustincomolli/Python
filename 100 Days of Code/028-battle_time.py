import os
import time

player1_name = "Agustín"
player1_type = ""
player1_health = 0
player1_strength = 0

player2_name = ""
player2_type = ""
player2_health = 0
player2_strength = 0

dice_1 = 0
dice_2 = 0
damage = 0
round_number = 1

default_color = "\033[0m"
red_color = "\033[31m"
green_color = "\033[32m"
yellow_color = "\033[33m"
blue_color = "\033[34m"
magenta_color = "\033[35m"
cyan_color = "\033[36m"


def roll_dice(sides):
    """
        DESCRIPTION: Genera una tirada de dados aleatoria.
        PARAMETERS:
                    - sides: son las cantidad de caras que tiene el dado.
    """
    import random

    return random.randint(1, sides)


def generate_health():
    """
        DESCRIPTION: Genera la cantidad de salud del personaje.
    """

    health = ((roll_dice(6) * roll_dice(12)) / 2) + 10
    return int(health)


def generate_strength():
    """
        DESCRIPTION: Genera la cantidad de fuerza del personaje.
    """

    strength = ((roll_dice(6) * roll_dice(8)) / 2) + 12
    return int(strength)


def show_character(name, type, health, strength):
    """
        DESCRIPTION: Muestra el personaje elegido.
        PARAMETERS: Son los datos del personaje.
    """

    print(f"\n*** {name} - {type} ***")
    print(f" - Salud  ❤️: {health}")
    print(f" - Fuerza 💪: {strength}")
    print(blue_color + "\nQue tu nombre pase a la Leyenda..." + default_color)


def show_status(name, type, health):
    """
        DESCRIPTION: Muestra el estado de salud del personaje.
        PARAMETERS: Son los datos del personaje.
    """

    print(f"\n*** {name} - {type} ***")
    print(f" - Salud  ❤️: {health}")


os.system("clear")
print(yellow_color + "⚔️ TIEMPO DE BATALLA ⚔️" + default_color)
print("\nCrea a tu personaje 🧑")

player1_name = input(default_color + "\nNombra a tu personaje: "
                     + green_color).capitalize()

player1_type = input(default_color +
                     "Elige una clase (Caballero 🛡️, Arquero 🏹," +
                     "Daguero 🗡️, Mago 🪄):" +
                     green_color).capitalize()
player1_health = generate_health()
player1_strength = generate_strength()

show_character(player1_name, player1_type, player1_health, player1_strength)

time.sleep(1)
print("\n¿Contra quién vas a luchar?\n")

player2_name = input(default_color + "\nNombra a tu personaje: "
                     + green_color).capitalize()

player2_type = input(default_color +
                     "Elige una clase (Caballero 🛡️, Arquero 🏹," +
                     "Daguero 🗡️, Mago 🪄):" +
                     green_color).capitalize()
player2_health = generate_health()
player2_strength = generate_strength()

show_character(player2_name, player2_type, player2_health, player2_strength)
time.sleep(2)

while True:
    os.system("clear")
    print(yellow_color + "⚔️ TIEMPO DE BATALLA ⚔️" + default_color)

    if round_number == 1:
        print("\n¡Que comience la pelea!\n")
    else:
        print("\n¡Continúa la pelea!\n")

    dice_1 = roll_dice(6)
    dice_2 = roll_dice(6)

    damage = abs(player1_strength - player2_strength) + 1

    if dice_1 > dice_2:
        player2_health -= damage
        print(f"{player1_name} gana el {round_number} round.")
        print(f"{player2_name} recibe un golpe con {damage} de daño.")
    elif dice_2 > dice_1:
        player1_health -= damage
        print(f"{player2_name} gana el {round_number} round.")
        print(f"{player1_name} recibe un golpe con {damage} de daño.")
    else:
        print("Ambos luchadores esquivan los golpes...")

    show_status(player1_name, player1_type, player1_health)
    show_status(player2_name, player2_type, player2_health)

    if player1_health < 1:
        print(red_color + f"\n{player1_name} a muerto ☠️🪦🧟" + default_color)
        print(f"\n{player2_name} destroza a " +
              f"{player1_name} en {round_number} round/s")
        break
    elif player2_health < 1:
        print(red_color + f"\n{player2_name} a muerto ☠️🪦🧟" + default_color)
        print(f"\n{player1_name} destroza a " +
              f"{player2_name} en {round_number} round/s")
        break
    else:
        print("\n¡Y ambos están de pie para la siguiente ronda!...")
        round_number += 1
        time.sleep(3)
