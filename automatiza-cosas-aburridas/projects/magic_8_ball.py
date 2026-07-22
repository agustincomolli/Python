"""
Ejemplo del juego Magic 8 Ball usando tuplas que es una estructura de datos
que no cambia y Python puede hacer optimizaciones para que el programa
funcione más rápido.
"""

import random

ANSWER = (
    "Es seguro",
    "Definitivamente sí",
    "Sí",
    "Respuesta vaga, inténtalo de nuevo",
    "Pregunta de nuevo más tarde",
    "Concéntrate y pregunta de nuevo",
    "Mi respuesta es no",
    "El panorama no es muy bueno",
    "Muy dudoso"
)

TOP_INDEX = len(ANSWER) - 1

print("Haz una pregunta que tenga como respuesta sí o no")
question = input("> ")
random_number = random.randint(0, TOP_INDEX)
print(ANSWER[random_number])
