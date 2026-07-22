"""
Ejemplo usando el módulo loggin para depurar programas
"""

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="debug_02.log",
                    format=" %(asctime)s - %(levelname)s - %(message)s")
logging.debug("Inicio del programa")


def factorial(number):
    """
    Devuelve el factorial de number.

    Args:
        number (int): Número que se quiere hacer el factorial.

    Returns:
        int: Resultado.
    """
    logging.debug("Inicio de factorial(%d)", number)
    total = 1
    for i in range(number + 1):
        total *= i
        logging.debug("i es: %d y total es: %d", i, total)
    logging.debug("Fin de factorial(%d)", number)
    return total


print(factorial(5))
logging.debug("Fin del programa")
