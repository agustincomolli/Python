"""
Ejemplo de variables locales y globales.
"""


def change_counter():
    """Incrementador de contador"""
    # Para modificar una variable global hay que anteponer la palabra global.

    # pylint: disable=global-statement
    global counter
    # pylint: disable=used-before-assignment
    counter = counter + 1


# pylint: disable=invalid-name
counter = 0
print("Valor de counter antes de llamar a la función:", counter)

change_counter()
print("Valor de counter después de llamar a la función:", counter)
