from mylib import clear_screen, color_me, input_color, press_enter_to_continue
from mylib import choose_option
import datetime


def add():
    clear_screen()
    print(color_me("🐦 Twistter 🐦\n", "yellow"))
    print(color_me("➕ Agregar twistter...\n"))
    twistters[datetime.datetime.now()] = input_color(
        "Tu twist: ", color_input="green")


def view():
    print(color_me("Ver twisters 🔍\n", "blue"))
    count = 1
    index = 1
    key_list = []
    for key in twistters.keys():
        key_list.append(key)

    key_list.sort(reverse=True)
    for key in key_list:
        print(f"{index}) {key}: {twistters[key]}")
        index += 1
        count += 1
        if count == 5:
            next_page = input_color("\n¿Mostrar otra página? S|N: ", color_input="green").lower()
            if not next_page == "s":
                return
            else:
                clear_screen()
                print(color_me("🐦 Twistter 🐦\n", "yellow"))
                print(color_me("Ver twisters 🔍\n", "blue"))
                count = 1

    print("\nNo hay más twisters para ver.")
    press_enter_to_continue()

title = color_me("🐦 Twistter 🐦", "yellow")
options = ["Agregar", "Ver", "Salir"]
twistters = {}

while True:
    selection = choose_option(title, options)
    if selection == 1:
        add()
    elif selection == 2:
        view()
    else:
        break
