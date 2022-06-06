# Juego de Piedra, Papel o Tijeras.
import random

# Estas variables realizan el seguimiento del número de victorias, derrotas
# y empates.
victorias = 0
derrotas = 0
empates = 0

while True:
    print("¡¡¡PIEDRA... PAPEL... O TIJERAS!!!")
    print(f"Victorias: {victorias}, Derrotas: {derrotas}, Empates: {empates}")
    jugador = input("Ingrese (p)iedra, pape(l), (t)ijeras, (s)alir: ")

    if jugador == "s":
        print("\n¡Chau, chau, adiós!")
        break
    elif jugador == "p":
        jugador = "piedra"
    elif jugador == "l":
        jugador = "papel"
    elif jugador == "t":
        jugador = "tijeras"
    else:
        continue

    maquina = random.choice(["piedra", "papel", "tijeras"])

    print(f"\n{jugador.capitalize()} VS...'{maquina.capitalize()}'\n")

    if jugador == maquina:
        resultado = "e"
    elif (jugador == "piedra") and (maquina == "papel"):
        resultado = "d"
    elif (jugador == "piedra") and (maquina == "tijeras"):
        resultado = "v"
    elif (jugador == "papel") and (maquina == "tijeras"):
        resultado = "d"
    elif (jugador == "papel") and (maquina == "piedra"):
        resultado = "v"
    elif (jugador == "tijeras") and (maquina == "piedra"):
        resultado = "d"
    elif (jugador == "tijeras") and (maquina == "papel"):
        resultado = "v"

    if resultado == "v":
        print("¡Ganaste!")
        victorias += 1
    elif resultado == "e":
        print("¡Empate!")
        empates += 1
    else:
        print("¡Perdiste!")
        derrotas += 1

    print()