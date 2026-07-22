"""
Ejemplo de la secuencia de Collatz
"""


def collatz(number):
    """
    Realiza el cálculo de la secuencia collatz a partir de number

    Args:
        number (int): número que empieza la secuencia.

    Returns:
        int: el siguiente número en la secuencia.
    """
    if number % 2 == 0:
        return number // 2

    return (number * 3) + 1


def input_int(prompt, error_message):
    """
    Valida la entrada del usuario para que ingrese un número entero.

    Args:
        prompt (str): mensaje que se mostrará al usuario para pedir que
                      ingrese un número.
        error_message (str): Mensaje de error al usuario.

    Returns:
        int: El número ingresado por el usuario.
    """
    while True:
        print(prompt)
        try:
            number = int(input("> "))
            return number
        except ValueError:
            print()
            print(error_message)
            print()


print("*** Secuencia de Collatz ***\n")

PROMPT = "Escribe un número para iniciar la secuencia de Collatz"
ERROR_MESSAGE = "ERROR: debes escribir un número."
number_input = input_int(PROMPT, ERROR_MESSAGE)

print()
print("-> ", number_input, end=" ")
while number_input != 1:
    number_input = collatz(number_input)
    print(number_input, end=" ")
