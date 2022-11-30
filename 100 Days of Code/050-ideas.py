from mylib import clear_screen, color_me, input_color, press_enter_to_continue
import time
import random


def show_menu():
    clear_screen()
    print(color_me("🌟 Generador de Ideas 🌟\n", "yellow"))
    print("1 - Agregar Idea")
    print("2 - Cargar una idea aleatoria")
    print("3 - Salir")

    return input_color("\nIngrese una opción: ", color_input="green")


def add_idea():
    clear_screen()
    print(color_me("🌟 Generador de Ideas 🌟\n", "yellow"))
    new_idea = input_color("\n👉 ", color_input="green")
    new_idea += "\n"

    file = open("./ideas.txt", mode="a", encoding="UTF-8")
    file.write(new_idea)
    file.close()
    print(color_me("\nIdea agregada...", "blue"))
    time.sleep(3)


def random_idea():
    clear_screen()
    print(color_me("🌟 Generador de Ideas 🌟\n", "yellow"))

    file = open("./ideas.txt", mode="r", encoding="UTF-8")
    ideas = file.read().splitlines()
    print("Idea aleatoria: " + color_me(random.choice(ideas), "cyan"))
    time.sleep(3)
    file.close()


while True:
    option = show_menu()

    if option == "1":
        add_idea()
    elif option == "2":
        random_idea()
    elif option == "3":
        break
    else:
        print(color_me("\nERROR: Debe ingresar una opción válida.", "red"))
        press_enter_to_continue()
        continue
