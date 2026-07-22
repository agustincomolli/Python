"""Ejemplo de depuración usando raise.

Este módulo contiene la función ``box_print`` que dibuja un cuadro
usando un símbolo dado y valida sus parámetros lanzando excepciones
cuando no cumplen las condiciones esperadas.
"""


def box_print(symbol, width, height):
    """Dibuja un cuadro usando un símbolo.

    Args:
        symbol (str): Un solo caracter que se usará como borde del cuadro.
        width (int): Ancho del cuadro (debe ser mayor que 2).
        height (int): Alto del cuadro (debe ser mayor que 2).

    Raises:
        ValueError: Si ``symbol`` no es una cadena de un solo caracter.
        ValueError: Si ``width`` o ``height`` son menores o iguales a 2.

    Examples:
        >>> box_print('*', 4, 4)
        ****
        *  *
        *  *
        ****
    """

    if len(symbol) != 1:
        raise ValueError("Symbol debe ser una cadena de un solo caracter.")
    if width <= 2:
        raise ValueError("Width debe ser mayor que 2.")
    if height <= 2:
        raise ValueError("Height debe ser mayor que 2.")

    print(symbol * width)
    for _ in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)


try:
    box_print("*", 4, 4)
    box_print("O", 20, 5)
    box_print("x", 1, 3)
    box_print("ZZ", 2, 3)
except ValueError as err:
    print("Ocurrió una excepción: " + str(err))

try:
    box_print('ZZ', 3, 3)
except ValueError as err:
    print('Ocurrió una excepción: ' + str(err))
