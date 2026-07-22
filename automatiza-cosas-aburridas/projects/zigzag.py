"""
Genera una barra de * que se mueve en zigzag.
"""

import time
import sys


def print_bar(spacing):
    """
    Imprime en pantalla una línea de asteriscos seguido de determinados
    espacios en blanco.

    Args:
        indent (int): La cantidad de espacios en blanco.
    """
    print((" " * spacing) + "********")
    time.sleep(.1)


indent = 0
is_increasing = True

print("Presione ENTER para comenzar y CTRL + C para terminar...")
input()

try:
    while True:
        print_bar(indent)
        if is_increasing:
            indent = indent + 1
            if indent == 20:
                # Cambia la dirección de la barra.
                is_increasing = False
        else:
            indent = indent - 1
            if indent == 0:
                is_increasing = True
except KeyboardInterrupt:
    sys.exit()
