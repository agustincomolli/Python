#!/usr/bin/env/ python3

import os


class TextStyles:
    # Códigos ANSI para dar estilos al texto.
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


class Colors:
    # Códigos ANSI para colorear el texto.
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    DEFAULT = "\033[0m"


class Align:
    LEFT = "l"
    CENTER = "c"
    RIGHT = "r"


def highlight_text(text: str, color_code: str = "", style_code: str = "") -> str:
    """
    Devuelve el texto especificado resaltado con el color y estilo ANSI indicados.

    Args:
        text (str): El texto que se desea resaltar.
        color_code (str, opcional): El código de color ANSI que se aplicará al texto.
                                    Puede ser uno de los códigos definidos en la clase
                                    Colors. (Por defecto es una cadena vacía).
        style_code (str, opcional): El estilo ANSI que se aplicará al texto.
                                    Puede ser uno de los estilos definidos en la clase
                                    TextStyles, como BOLD, ITALIC o UNDERLINE. 
                                    (Por defecto es una cadena vacía).

    Returns:
        str: El texto especificado resaltado con el color y estilo indicados.    
    """
    return f"{color_code}{style_code}{text}{Colors.DEFAULT}"


def align_text(text: str, align: str = Align.LEFT, width: int = None)->str:
    """
    Devuelve el texto especificado alineado según la opción indicada.

    Args:
        text (str): El texto que se desea alinear.
        align (str, opcional): La opción de alineación deseada. Puede ser
                               Align.LEFT (izquierda), Align.CENTER (centro) o
                               Align.RIGHT (derecha). (Por defecto es Align.LEFT).
        width (int, opcional): El ancho deseado para el texto alineado. Si no se
                               proporciona, se utilizará el ancho de la terminal.

    Returns:
        str: El texto especificado alineado según la opción y ancho indicados.
    
    """
    if width is None or width <= 0:
        width = get_terminal_size()[0]
    if align == Align.RIGHT:
        return text.rjust(width)
    elif align == Align.CENTER:
        return text.center(width)
    else:
        return text.ljust(width)


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
    value = input(highlight_text(message, color_input))
    print(Colors.DEFAULT, end="")  # Reset the color to the default

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
    input("Presione " + highlight_text("ENTER", Colors.YELLOW) + " para continuar...")


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
        choice = input(highlight_text("\nElija una opción: ", color_input))
        print(Colors.DEFAULT, end="")  # Reset the color to the default

        # Verifica que la opción sea válida
        if choice.isdigit() and int(choice) > 0 and int(choice) <= len(options):
            # return options[int(choice)-1]
            return int(choice)
        else:
            print(highlight_text("\nOpción inválida, intente de nuevo.", Colors.RED))
            press_enter_to_continue()


def show_error(message: str):
    """
    Muestra un mensaje de error de manera más visual.

    Args:
        message (str): Mensaje de error a mostrar.

    """

    print(highlight_text("ERROR: ", Colors.RED) + message)


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
        response = input(f"{highlight_text(message, Colors.YELLOW)}\n" +
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
