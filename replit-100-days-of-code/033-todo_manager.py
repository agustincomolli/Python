import os
import time


def color_me(text, color):
    """
        DESCRIPTION: Devuelve un texto, con el código del color seleccionado.\n
        PARAMETERS:\n 
                    - text: es el texto a colorear
                    - color: red, green, yellow, blue, magenta o cyan.
    """
    default_color = "\033[0m"
    red_color = "\033[31m"
    green_color = "\033[32m"
    yellow_color = "\033[33m"
    blue_color = "\033[34m"
    magenta_color = "\033[35m"
    cyan_color = "\033[36m"

    if color == "red":
        color = red_color
    elif color == "green":
        color = green_color
    elif color == "blue":
        color = blue_color
    elif color == "yellow":
        color = yellow_color
    elif color == "magenta":
        color = magenta_color
    elif color == "cyan":
        color = cyan_color
    else:
        color = default_color

    return color + text + default_color


def view_menu():
    menu = ["1 - Agregar tarea", "2 - Eliminar tarea", "3 - Ver lista",
            "4 - Salir"]
    for item in menu:
        print(item)
    print()


def view_list():
    """
        DESCRIPTION: Imprime la lista de tareas.
    """
    print()
    for item in todo_list:
        print(item)
    print()
    time.sleep(3)


todo_list = []

while True:
    os.system("clear")
    print(color_me("*** Cosas para Hacer ***\n", "yellow"))

    time.sleep(0.5)
    view_menu()
    time.sleep(0.5)
    answer = input(color_me("Ingrese su opción: ", "blue"))

    if answer == "1":
        item = input("¿Qué desea agregar?\n> ")
        todo_list.append(item)
    elif answer == "2":
        item = input("¿Qué tarea desea eliminar?\n> ")
        if item in todo_list:
            todo_list.remove(item)
        else:
            print("Esa tarea no está en la lista. 🙄")
    elif answer == "3":
        view_list()
    elif answer == "4":
        print("\n¡Adiós! 👋")
        break
    else:
        print("\nNo entiendo lo que quieres hacer... 🤔")

    time.sleep(2)
