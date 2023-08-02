# console_text_utils.py

import os


# Función para limpiar la consola
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Función para centrar el texto en la consola
def center_text(text, width=None):
    if width is None:
        width = os.get_terminal_size().columns
    return text.center(width)


# Función para alinear el texto a la izquierda en la consola
def left_align_text(text, width=None):
    if width is None:
        width = os.get_terminal_size().columns
    return text.ljust(width)


# Función para alinear el texto a la derecha en la consola
def right_align_text(text, width=None):
    if width is None:
        width = os.get_terminal_size().columns
    return text.rjust(width)


# Función para resaltar el texto con colores ANSI
def highlight_text(text, color_code):
    return f"{color_code}{text}\033[0m"


# Colores ANSI para resaltar el texto
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


# Función para obtener la entrada del usuario con un mensaje y validación opcional
def get_user_input(prompt, validator_func=None):
    while True:
        user_input = input(prompt)
        if validator_func is None or validator_func(user_input):
            return user_input
        print("Entrada inválida. Inténtalo de nuevo.")


# Ejemplo de función de validación que comprueba si la entrada es un número entero
def validate_integer_input(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False
