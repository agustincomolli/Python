import mis_emojis
from datetime import *
from random import randint

def tirar_dado():
    """Generar un número aleatorio entre 1 y 6"""
    tirada = randint(1, 6)
    print(f"{mis_emojis.python}  hizo un {mis_emojis.dado}")
    print(f"Tiraste el dado y has sacado {tirada}")
    print(f"{mis_emojis.fuego * tirada}")


def preguntar_pasatiempos():
    """Preguntar por un pasatiempos y mostrar un respuesta."""
    pasatiempo = input("¿Qué te gusta hacer?: ")
    print(f"¡Eso suena {mis_emojis.diversión}  !")
    print(f"Podrías hacer un proyecto en {mis_emojis.python}  sobre {pasatiempo}.")


print("\nDi hola:\n" + "*" * 8)
print(f"¡Hola! {mis_emojis.mundo}")
print(f"Bienvenido a {mis_emojis.python}")

print("\nSumas y fechas:\n" + "*" * 15)
print(f"Python es muy bueno para {mis_emojis.sumas}")
print(f"(2 + 4) * (5 + 3) = {(2 + 4) * (5 + 3)}")
print(f"\nLa {mis_emojis.calendario} y la {mis_emojis.reloj} actual es: {datetime.now()}")

print("\nRodar un dado:\n" + "*" * 14)
# Llamar a la función tirar_Dado().
tirar_dado()

print("\nArrancador de oraciones:\n" + "*" * 24)
print(f"Yo {mis_emojis.corazón}  comer")
print(f"Tomar {mis_emojis.mate} me hace {mis_emojis.feliz}")
print(f"Quiero hacer juego con {mis_emojis.python}\n")

print("\nPasatiempos:\n" + "*" * 12)
preguntar_pasatiempos()