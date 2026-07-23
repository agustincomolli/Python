from mylib import clear_screen, color_me, input_color, press_enter_to_continue
import random
import time

cards = {
    "Chewbacca": {
        "Altura": 2.28,
        "Inteligencia": 12,
        "Lado oscuro": 5,
        "Poderes Jedi": 10,
        "Habilidades de batalla": 55,
        "Factor Fuerza": 4
    },
    "Darth Vader": {
        "Altura": 2.02,
        "Inteligencia": 16,
        "Lado oscuro": 22,
        "Poderes Jedi": 82,
        "Habilidades de batalla": 55,
        "Factor Fuerza": 4
    },
    "Emperador": {
        "Altura": 1.73,
        "Inteligencia": 14,
        "Lado oscuro": 25,
        "Poderes Jedi": 95,
        "Habilidades de batalla": 25,
        "Factor Fuerza": 5
    },
    "Han Solo": {
        "Altura": 2.28,
        "Inteligencia": 12,
        "Lado oscuro": 5,
        "Poderes Jedi": 10,
        "Habilidades de batalla": 55,
        "Factor Fuerza": 4
    },
    "Lando Calrissian": {
        "Altura": 1.8,
        "Inteligencia": 13,
        "Lado oscuro": 6,
        "Poderes Jedi": 4,
        "Habilidades de batalla": 50,
        "Factor Fuerza": 3
    },
    "Luke Skywalker": {
        "Altura": 1.72,
        "Inteligencia": 15,
        "Lado oscuro": 4,
        "Poderes Jedi": 90,
        "Habilidades de batalla": 43,
        "Factor Fuerza": 4
    },
    "Obi-Wan Kenobi": {
        "Altura": 1.75,
        "Inteligencia": 18,
        "Lado oscuro": 1,
        "Poderes Jedi": 80,
        "Habilidades de batalla": 26,
        "Factor Fuerza": 6
    },
}


def show_menu():
    clear_screen()

    print(color_me(f"{'🌟 STAR WARS 🌟':^30}", "yellow"))
    print(color_me("\nPersonajes: ", "blue"))

    index = 1
    for key in cards.keys():
        print(f"    {index} - {key}")
        index += 1

    option = input_color("\nSeleccione un personaje: (s = salir) 👉 ",
                         color_input="green")

    if not option.isnumeric():
        if option == "s":
            return option
        else:
            return None

    option = int(option)
    if option < 0 or option > len(cards):
        return None
    else:
        return list(cards)[option-1]


def choose_stat():
    clear_screen()

    print(color_me(f"{'🌟 STAR WARS 🌟':^30}", "yellow"))
    print(color_me("\nEstadísticas: ", "blue"))

    print(f"    {'1 - Altura':<17} | {'2 - Inteligencia':^30} | " +
          "3 - Lado oscuro")
    print(
        f"    {'4 - Poderes Jedi':<18}| {'5 - Habilidades de batalla':^31} " +
        "| 6 - Factor Fuerza")

    option = input_color(
        "Elige la estadística con la que deseas comparar: ", color_input="green")
    if not option.isnumeric():
        return None

    option = int(option)
    if option < 1 or option > 6:
        return None
    elif option == 1:
        return "Altura"
    elif option == 2:
        return "Inteligencia"
    elif option == 3:
        return "Lado oscuro"
    elif option == 4:
        return "Poderes Jedi"
    elif option == 5:
        return "Habilidades de batalla"
    elif option == 6:
        return "Factor Fuerza"


while True:
    player_char = show_menu()

    if player_char == "s":
        break
    elif player_char == None:
        print(color_me("No has seleccionado una opción válidad. " +
                       "Intenta de nuevo...", "red"))
        time.sleep(3)
        continue

    print(f"\nHas seleccionado a {color_me(player_char, 'cyan')}.")

    computer_char = random.choice(list(cards))
    print(f"La computadora ha elegido a {color_me(computer_char, 'magenta')}")
    time.sleep(3)

    stat = None
    while stat == None:
        stat = choose_stat()
        if stat == None:
            print(color_me("No has seleccionado una opción válidad. " +
                           "Intenta de nuevo...", "red"))
            time.sleep(3)

    print(f"\nTú {player_char}, tienes {cards[player_char][stat]} de {stat}")
    print(f"La computadora {computer_char}, tiene " +
          f"{cards[computer_char][stat]} de {stat}")
    if cards[player_char][stat] > cards[computer_char][stat]:
        print(color_me("\n¡HAS GANADO! 🥳\n", "cyan"))
    else:
        print(color_me("\n¡HAS PERDIDO! 😢\n", "magenta"))

    press_enter_to_continue()
