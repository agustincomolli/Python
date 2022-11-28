from mylib import clear_screen, color_me, input_color
import random

cards = {
    "Chewbacca": {
        "height": 2.28,
        "intelligence": 12,
        "dark-side": 5,
        "jedi-powers": 10,
        "battle-skills": 55,
        "force-factor": 4
    },
    "Darth Vader": {
        "height": 2.02,
        "intelligence": 16,
        "dark-side": 22,
        "jedi-powers": 82,
        "battle-skills": 55,
        "force-factor": 4
    },
    "Emperador": {
        "height": 1.73,
        "intelligence": 14,
        "dark-side": 25,
        "jedi-powers": 95,
        "battle-skills": 25,
        "force-factor": 5
    },
    "Han Solo": {
        "height": 2.28,
        "intelligence": 12,
        "dark-side": 5,
        "jedi-powers": 10,
        "battle-skills": 55,
        "force-factor": 4
    },
    "Lando Calrissian": {
        "height": 1.8,
        "intelligence": 13,
        "dark-side": 6,
        "jedi-powers": 4,
        "battle-skills": 50,
        "force-factor": 3
    },
    "Luke Skywalker": {
        "height": 1.72,
        "intelligence": 15,
        "dark-side": 4,
        "jedi-powers": 90,
        "battle-skills": 43,
        "force-factor": 4
    },
    "Obi-Wan Kenobi": {
        "height": 1.75,
        "intelligence": 18,
        "dark-side": 1,
        "jedi-powers": 80,
        "battle-skills": 26,
        "force-factor": 6
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

    option = input_color("\nSeleccione un personaje: 👉 ", color_input="green")

    if not option.isnumeric():
        return None

    option = int(option)
    if option < 0 or option > len(cards)-1:
        return None
    else:
        return list(cards)[option - 1]


def choose_stat():
    clear_screen()

    print(color_me(f"{'🌟 STAR WARS 🌟':^30}", "yellow"))
    print(color_me("\nEstadísticas: ", "blue"))

    print(f"    {'1 - Altura':<17} | {'2 - Inteligencia':^30} | 3 - Lado oscuro")
    print(f"    {'4 - Poderes Jedi':<18}| {'5 - Habilidades de batalla':^31}| 6 - Factor Fuerza")


character = show_menu()
print(f"\nHas seleccionado a {color_me(character, 'cyan')}.")

computer = random.choice(list(cards))
print(f"La computadora ha elegido a {color_me(computer, 'magenta')}")

choose_stat()