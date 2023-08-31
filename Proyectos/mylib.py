#!/usr/bin/env/ python3

import os

# Diccionario que contiene los códigos de colores ANSI y sus nombres
# correspondientes.
colors = {
    "default": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m"
}


def get_color_code(color: str) -> str:
    """
    Devuelve el código de color ANSI para el color especificado.

    Args:
        color (str): El nombre del color (por ejemplo, "red", "green", etc.)

    Returns:    El código de color ANSI para el color especificado, o el código
                de color predeterminado si el color no se reconoce.

    """
    return colors.get(color, colors["default"])


def color_me(text: str, color: str = "") -> str:
    """
    Devuelve el texto especificado con el código de color ANSI especificado.

    Args:
        text (str):  El texto a colorear.
        color (str): El nombre del color a usar (green, red, blue, yellow, 
                     cyan, magenta)

    Returns:    El texto especificado con el código de color ANSI especificado.

    """
    color_code = get_color_code(color)

    return color_code + text + colors["default"]


def input_color(message: str, color_input: str = "") -> str:
    """
    Muestra un mensaje al usuario con un mensaje coloreado y acepta la entrada 
    del usuario con una solicitud coloreada.

    Args:
        message (str):     El mensaje a mostrar al usuario.
        color_input (str): El nombre del color a usar para la solicitud
                           de entrada (por ejemplo, "red", "green", etc.)

    Returns:    La entrada del usuario.

    """
    color_code = get_color_code(color_input)
    value = input(message + color_code)
    print(colors["default"], end="")  # Reset the color to the default

    return value


def clear_screen():
    """
    Limpia la pantalla de acuerdo al sistema operativo.

    """

    # posix = Linux or MAC
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def get_terminal_size() -> tuple:
    """
    Devuelve las medidas de la terminal donde se está ejecutando el programa.

    Returns:
        tuple: ancho y alto de la terminal.

    """
    size = os.get_terminal_size()
    width = size.columns
    height = size.lines

    return width, height


def press_enter_to_continue():
    """
    Muestra un mensaje que solicita al usuario que presione "Enter" para 
    continuar.

    """
    input("Presione " + color_me("ENTER", "yellow") + " para continuar...")


def choose_option(title: str, options: list, color_input: str = "") -> int:
    """
    Muestra un menú con las opciones especificadas y solicita al 
                 usuario que elija una opción.

    Args:
        title (str):    El título del menú
        options (str):  Una lista de opciones a mostrar en el menú.

    Returns:    La opción seleccionada por el usuario.

    """
    while True:
        clear_screen()
        print(title + "\n")

        for i, option in enumerate(options):
            print(f"{i+1} - {option}")

        # Solicita al usuario que elija una opción
        color_code = get_color_code(color_input)
        choice = input("\nElija una opción: " + color_code)
        print(colors["default"], end="")  # Reset the color to the default

        # Verifica que la opción sea válida
        if choice.isdigit() and int(choice) > 0 and int(choice) <= len(options):
            # return options[int(choice)-1]
            return int(choice)
        else:
            print(color_me("\nOpción inválida, intente de nuevo.", "red"))
            press_enter_to_continue()


def show_error(message: str):
    """
    Muestra un mensaje de error de manera más visual.

    Args:
        message (str): Mensaje de error a mostrar.

    """

    print(color_me("ERROR: ", "red") + message)


def warning(message: str) -> bool:
    """
    Muestra un mensaje de advertencia al usuario y solicita una respuesta 
    afirmativa o negativa.

    Args:
        message (str): Mensaje de advertencia a mostrar.

    Returns: 
        bool: True si el usuario responde afirmativamente, False en caso contrario.

    """

    while True:
        response = input(f"{color_me(message, 'yellow')}\n" +
                         "¿Desea continuar? (s/n) ").lower()
        if response == "s":
            return True
        elif response == "n":
            return False


def confirm(message: str) -> bool:
    """
    Muestra un mensaje de confirmación al usuario y solicita una respuesta 
    afirmativa o negativa.

    Args:
        message (str): Mensaje de confirmación a mostrar.

    Returns:    
        bool: True si el usuario responde afirmativamente, False en caso contrario.

    """

    while True:
        response = input(f"{message} (s/n) ").lower()
        if response == "s":
            return True
        elif response == "n":
            return False
