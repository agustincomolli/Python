"""
Manejo de excepciones.
"""


def division(dividend, divisor):
    """
    Devuelve la división de dos números.

    Args:
        dividend (float): El número que será dividido.
        divisor (float): El número por el cual se divide.

    Returns:
        float: Resultado
    
    Raises:
        ZeroDivisionError: Si el divisor es igual a cero.
    """
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print("ERROR: no se puede dividir un número por 0")
        return None


print(division(42, 2))
print(division(42, 12))
print(division(42, 0))
print(division(42, 1))
