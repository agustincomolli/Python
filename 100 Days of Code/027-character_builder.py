import os
import time

character_name = ""
character_type = ""
health = 0
strength = 0
answer = ""

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

    return int(((roll_dice(6) * roll_dice(12)) / 2) + 10)


def generate_strength():
    """
        DESCRIPTION: Genera la cantidad de fuerza del personaje.
    """

    return int(((roll_dice(6) * roll_dice(8)) / 2) + 12)


def generate_character():
    """
        DESCRIPTION: Genera la cantidad de fuerza del personaje.
    """
    while True:
        name = input(default_color +
                               "\nNombra a tu personaje: " + green_color)

        if name == "":
            print(red_color + "\nDebes ingresar algún nombre. " +
                  "Inténtalo de nuevo." + default_color)
            time.sleep(2)
            continue

        type = input(default_color +
                               "Elige una clase (Caballero 🛡️, Arquero 🏹," +
                               "Daguero 🗡️, Mago 🪄):" +
                               green_color).capitalize()

        if type not in ["Caballero", "Arquero", "Daguero", "Mago"]:
            print(red_color + "\nNo has ingresado un clase válida. " +
                  "Inténtalo de nuevo." + default_color)
            time.sleep(2)
            continue

        # Si pasa las dos validaciones, salir del ciclo.
        print(default_color, end="")
        return name, type


while True:
    os.system("clear")

    print(yellow_color + "⚔️ Constructor de Personajes ⚔️" + default_color)

    character_name, character_type = generate_character()
    health = generate_health()
    strength = generate_strength()

    print(f"\n*** {character_name.capitalize()} ***\n")
    print(f" - Salud  ❤️: {health}")
    print(f" - Fuerza 💪: {strength}")
    print(blue_color + "\nQue tu nombre pase a la Leyenda..." + default_color)

    answer = input("\n¿Generar otro personaje? [s|n] " + green_color).lower()
    print(default_color, end="")
    if answer == "n":
        break
