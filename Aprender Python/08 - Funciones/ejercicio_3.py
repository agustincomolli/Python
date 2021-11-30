# Llama al método create_baraja() del módulo baraja
print("\nPaso 1: \n********")

import baraja

cartas = baraja.crear_baraja()

for carta in cartas:
    print(carta)