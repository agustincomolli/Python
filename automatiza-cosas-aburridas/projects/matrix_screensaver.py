"""
Simula el protector de pantallas de la película Matrix.
"""

import random
import sys
import time
import os

# Número de columnas.
WIDTH = os.get_terminal_size().columns

try:
    # Para cada columna, cuando el contador es 0, no se muestra ninguna secuencia.
    # De lo contrario, funciona como un contador que indica cuántas veces debe
    # mostrarse un 1 o un 0 en esa columna.
    columns = [0] * WIDTH

    while True:
        # Recorrer cada columna.
        for i in range(WIDTH):
            if random.random() < 0.02:
                # Reiniciar un contador de flujo en esta columna.
                # La longitud del flujo está entre 4 y 14 caracteres.
                columns[i] = random.randint(4, 14)

            # Imprimir un caracter en esa columna
            if columns[i] == 0:
                print(" ", end="")
            else:
                # Imprimir 0 o 1.
                print(random.choice([0, 1]), end="")
                # Decrementar el contador para esta columna.
                columns[i] -= 1

        # Agregar un salto de línea
        print()
        # Cada fila se detiene durante una décima de segundo.
        time.sleep(0.1)
except KeyboardInterrupt:
    # Al presionar Ctrl + C, salir del programa
    sys.exit()
