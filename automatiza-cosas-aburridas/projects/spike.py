"""
Animación de desplazamiento que dibuja picos.
"""
import time
import sys


def draw_spike():
    """
    Dibuja la animación de un pico visto de forma horizontal.
    """
    for i in range(1, 9):
        print("-" * (i * i))
        time.sleep(.1)

    for i in range(7, 1, -1):
        print("-" * (i * i))
        time.sleep(.1)


print("*** SPIKE ***")
print("Presione ENTER para comenzar y CTRL + C para finalizar...")
input()

try:
    while True:
        draw_spike()
except KeyboardInterrupt:
    sys.exit()
