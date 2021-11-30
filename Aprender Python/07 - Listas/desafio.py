import random

palos_de_carta = ["Corazones", "Diamantes", "Tréboles", "Picas"]
numeros_de_carta = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "As"]
maso_de_cartas = []

for palo in palos_de_carta:
    for numero in numeros_de_carta:
        maso_de_cartas.append(f"{numero} de {palo}")

print(f"Hay {len(maso_de_cartas)} cartas en el maso.")

print("Repartiendo...")

mano_del_jugador = random.choices(maso_de_cartas, k=5)

# Eliminar las cartas dadas al jugador del maso.

for carta in mano_del_jugador:
    maso_de_cartas.remove(str(carta))

print(f"Hay {len(maso_de_cartas)} cartas en el maso.")

print(f"El jugador tiene las siguientes cartas en su mano: \n{mano_del_jugador}")