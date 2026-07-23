default_color = "\033[0m"
red_color = "\033[31m"
green_color = "\033[32m"
yellow_color = "\033[33m"


def roll_dice(sides):
    """
        DESCRIPTION: Devuelve un valor aleatorio entre 1 y 'sides' que simula
        el lanzamiento de un dados de n caras.
        PARAMETERS: 
            sides - Integer que simula la cantidad de caras de un dado.
    """
    import random

    return random.randint(1, sides)


def generate_stats():
    """
        DESCRIPTION: Genera de forma aleatoria un número entero que va
        a representar la cantidad de vida de un jugador.
    """
    dice_6_sides = roll_dice(6)
    dice_8_sides = roll_dice(8)

    return dice_6_sides * dice_8_sides


print(yellow_color + "⚔️ Generador de Estado de Vida ⚔️\n" + default_color)

while True:
    player_name = input("Nombre del jugador: " + green_color)
    print(red_color + f"Su nivel de vida es de {generate_stats()} ❤️" + default_color)

    continue_adding = input("\n¿Agregar otro jugador [s|n]? ").lower()
    if continue_adding != "s":
        break