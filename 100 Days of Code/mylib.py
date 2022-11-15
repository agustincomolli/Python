import os


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


def clear_screen():
    """
        DESCRIPTION: Limpiar la pantalla según el sistena operativo.
                     posix = Linux o MAC
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
