"""
Ejemplo de funciones con valores de retorno creando un programa con el
juego Magic 8 Ball.
"""

import random


def get_answer(answer_number):
    """
    Devuelve una respuesta de Magic 8 Ball según el número pasado.
    Args:
        answer_number (int): número entre 1 y 9
    Returns:
        str: una cadena de texto con la respuesta correspondiente.
    """

    mesage = ""

    if answer_number == 1:
        mesage = "Es seguro"
    elif answer_number == 2:
        mesage = "Definitivamente sí"
    elif answer_number == 3:
        mesage = "Sí"
    elif answer_number == 4:
        mesage = "Respuesta vaga, inténtalo de nuevo"
    elif answer_number == 5:
        mesage = "Pregunta de nuevo más tarde"
    elif answer_number == 6:
        mesage = "Concéntrate y pregunta de nuevo"
    elif answer_number == 7:
        mesage = "Mi respuesta es no"
    elif answer_number == 8:
        mesage = "El panorama no es muy bueno"
    elif answer_number == 9:
        mesage = "Muy dudoso"

    return mesage


print("Haz una pregunta que tenga como respuesta sí o no")
question = input("> ")
random_number = random.randint(1, 9)
ANSWER = get_answer(random_number)
print(ANSWER)
