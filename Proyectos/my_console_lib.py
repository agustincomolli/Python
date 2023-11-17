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


def highlight_text(text: str, color: Colors = "", style: TextStyles = "") -> str:
    """
    Devuelve el texto especificado resaltado con el color y estilo ANSI indicados.

    Args:
        text (str): El texto que se desea resaltar.
        color (Color, opcional): El código de color ANSI que se aplicará al texto.
                                    Puede ser uno de los códigos definidos en la clase
                                    Colors. (Por defecto es una cadena vacía).
        style (TextStyles, opcional): El estilo ANSI que se aplicará al texto.
                                    Puede ser uno de los estilos definidos en la clase
                                    TextStyles, como BOLD, ITALIC o UNDERLINE. 
                                    (Por defecto es una cadena vacía).

    Returns:
        str: El texto especificado resaltado con el color y estilo indicados.    
    """
    return f"{color}{style}{text}{Colors.DEFAULT}{TextStyles.RESET}"


def print_title(text: str, color: Colors = "", underline_char: str = "*") -> None:
    """
    Imprime un título con una línea subrayada.

    Args:
        text (str): El texto del título.
        color (Colors): Es el código del color
        underline_char (str): El carácter utilizado para subrayar el título.
    """
    title = f"{highlight_text(text, color)}"
    underline = f"\n{highlight_text(underline_char, color) * (len(text) + 1)}"

    print(title, underline)


def align_text(text: str, align: str = Align.LEFT, width: int = None) -> str:
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


def input_color(message: str, color_message: Colors = "", color_input: Colors = "") -> str:
    """
    Solicita un input al usuario mostrando el mensaje en un color y la respuesta en otro color.

    Args:
        message (str): El mensaje a mostrar al usuario.
        color_message: El color en el que se mostrará el mensaje.
        color_input: El color en el que se mostrará la respuesta del usuario.

    Returns: 
        str: La respuesta del usuario.
    """

    # Coloreamos el mensaje.
    message_colored = f"{color_message}{message}{color_input}"

    # Solicitamos el input al usuario.
    user_input = input(message_colored)
    print(Colors.DEFAULT, end="")

    # Devolvemos la respuesta del usuario con el color por defecto.
    return f"{user_input}"


def clear_screen():
    """
    Esta función borra el contenido actual en la consola/terminal.

    Este método funciona en diferentes sistemas operativos (Windows y Unix/Linux/MacOS), 
    y utiliza comandos del sistema específicos para cada uno de ellos para borrar la pantalla.

    Ejemplo de uso:
    >>> clear_screen()
    # Borra el contenido de la consola
    """

    # `os.name` es `'nt'` si el sistema operativo es Windows
    # Entonces, si estamos en Windows, usamos el comando `'cls'` para borrar la pantalla
    # De lo contrario, suponemos que estamos en un sistema tipo Unix (Linux/MacOS),
    # por lo que usamos el comando `'clear'` para borrar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')


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
    message = f"Presione {highlight_text("ENTER",Colors.YELLOW)} para continuar..."
    input(message)


def choose_option(title: str, options: list, color_input: Colors = Colors.DEFAULT) -> int:
    """
    Muestra un menú con las opciones especificadas y solicita al 
                 usuario que elija una opción.

    Args:
        title (str):    El título del menú
        options (list):  Una lista de opciones a mostrar en el menú.

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


def print_table(headers, data, borders=False):
    """
    Imprime datos en formato de tabla.

    Args:
        headers (list): Lista de encabezados de la tabla.
        data (list): Lista de listas con los datos de la tabla.
        borders (bool, opcional): True si se deben agregar bordes a la tabla, 
                                  False en caso contrario.
                                  Por defecto es True.
    """
    if not headers or not data:
        print("No hay datos para imprimir.")
        return

    max_lengths = [len(str(header)) for header in headers]

    for row in data:
        for i, value in enumerate(row):
            max_lengths[i] = max(max_lengths[i], len(str(value)))

    if borders:
        horizontal_line = "+-" + \
            "-".join("-" * length + "-+" for length in max_lengths)[:-1]
        print(horizontal_line)

    header_line = "| " + \
        " | ".join(f"{header:<{max_lengths[i]}}" for i,
                   header in enumerate(headers)) + " |"
    print(header_line)

    if borders:
        print(horizontal_line)

    for row in data:
        data_line = "| " + \
            " | ".join(
                f"{value:<{max_lengths[i]}}" for i, value in enumerate(row)) + " |"
        print(data_line)

    if borders:
        print(horizontal_line)
