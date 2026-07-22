"""
Escribe un programa para saber con qué frecuencia aparece una racha de seis 
caras o seis cruces en una lista generada aleatoriamente de 100 caras y cruces. 
Tu programa debería dividir el experimento en dos partes: la primera parte 
genera una lista de 100 valores de 'H' y 'T' seleccionados aleatoriamente, 
y la segunda parte comprueba si hay una racha. Pon todo este código en un 
bucle que repita el experimento 10.000 veces para que puedas saber qué 
porcentaje de los lanzamientos de moneda contiene una racha de seis caras 
o seis cruces seguidas. Como pista, la llamada de función random.randint(0, 1) 
devolverá un valor 0 el 50 por ciento de las veces y un valor 1 el otro 
50 por ciento.

Puedes empezar con la siguiente plantilla:
"""

import random

LIST_LIMIT = 100
number_of_streaks = 0

for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    streaks_list: list[str] = []
    for i in range(LIST_LIMIT):
        streaks_list.append(random.choice(["H", "T"]))

    # Code that checks if there is a streak of 6 heads or tails in a row
    for i in range(LIST_LIMIT):
        if ["H"] * 6 == streaks_list[i:i + 6] or ["T"] * 6 == streaks_list[i:i + 6]:
            number_of_streaks += 1
            break

print(f'Chance of streak: {(number_of_streaks / 100):.2f}%')
