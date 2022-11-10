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


def input_color(message, color_message="", color_input=""):
    """
        DESCRIPTION: Crea un input que tiene el mensaje en color y el texto
                     de entrada en color.\n
        PARAMETERS:\n
                    - message: es el texto del mensaje al usuario.
                    - color_message y color_input: red, green, yellow, blue,
                      magenta o cyan.
    """

    default_color = "\033[0m"
    red_color = "\033[31m"
    green_color = "\033[32m"
    yellow_color = "\033[33m"
    blue_color = "\033[34m"
    magenta_color = "\033[35m"
    cyan_color = "\033[36m"

    if color_input == "red":
        color_input = red_color
    elif color_input == "green":
        color_input = green_color
    elif color_input == "blue":
        color_input = blue_color
    elif color_input == "yellow":
        color_input = yellow_color
    elif color_input == "magenta":
        color_input = magenta_color
    elif color_input == "cyan":
        color_input = cyan_color
    else:
        color_input = default_color

    value = input(color_me(message, color_message) + color_input)
    print(default_color, end="")

    return value


def view():
    """
        DESCRIPTION: Imprime en pantalla la lista de cosas por hacer.
    """

    print("\nLista de tareas pendientes:\n")
    for item in todo_list:
        print(f"    - {item}")
    print()

    time.sleep(3)


def add():
    """
        DESCRIPTION: Agrega un item a la lista.
    """

    new_item = input_color("\n¿Qué desea agregar?\n> ", "", "green")
    if new_item in todo_list:
        print(color_me("\nEsa tarea ya se encuentra en la lista", "red"))
        time.sleep(3)
    else:
        todo_list.append(new_item)

    print()


def edit():
    """
        DESCRIPTION: Edita un elemento de la lista.
    """

    edit_item = input_color("\n¿Qué tarea desea editar?\n> ", "", "green")
    if edit_item in todo_list:
        idx = todo_list.index(edit_item)
        edit_item = input_color("\n¿Qué desea agregar?\n> ", "", "green")
        if edit_item in todo_list:
            print(color_me("\nEsa tarea ya se encuentra en la lista", "red"))
            time.sleep(3)
        else:
            todo_list[idx] = edit_item

    else:
        print(color_me("\nNo se encuentra esa tarea en la lista\n", "red"))
        time.sleep(3)


def delete():
    """
        DESCRIPTION: Elimina un elemento de la lista.
    """

    remove_item = input_color("\n¿Qué tarea desde eliminar?\n> ", "", "green")
    if remove_item in todo_list:
        confirmation = input_color("\n¿Está seguro de que quiere borrar" +
                                   f" \"{remove_item}\"? [s|n]\n" +
                                   color_me("> ", ""), "magenta", "green")

        if confirmation == "s":
            todo_list.remove(remove_item)
    else:
        print(color_me("Esa tarea no está en la lista", "red"))
        time.sleep(3)


todo_list = []

while True:
    os.system("clear")

    print(color_me("*** Administrador de lista de tareas pendientes: ***\n",
                   "yellow"))
    time.sleep(0.5)

    menu_text = "¿Desea ver, agregar, editar, eliminar una tarea o " + \
                "borrar la lista de tareas pendientes?\n> "
    selected_option = input_color(menu_text, "", "green")

    if selected_option == "ver":
        view()
    elif selected_option == "agregar":
        add()
    elif selected_option == "editar":
        edit()
    elif selected_option == "eliminar":
        delete()
    elif selected_option == "borrar":
        confirmation = input_color("\n¿Está seguro de que quiere borrar" +
                                   " TODA la lista? [s|n]\n" +
                                   color_me("> ", ""), "magenta", "green")

        if confirmation == "s":
         todo_list = []
    elif selected_option == "salir":
        break
