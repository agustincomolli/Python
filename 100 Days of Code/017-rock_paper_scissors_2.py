from getpass import getpass as input

player_1_victories = 0
player_2_victories = 0
round = 0
winner = 0

print("*** Batalla 🪨 📄✂️  Epica ***")

while True:
    round += 1
    print(f"\nRound {round}:")
    print("\nElija una opción 🪨  = R, 📄 = P, ✂️  = T\n")

    player_1 = input("Jugador 1: ").upper()
    player_2 = input("Jugador 2: ").upper()

    if player_1 == player_2:
        message = "¡Empate!"
        winner = 0
    elif player_1 == "R":
        if player_2 == "T":
            message = "¡El Jugador 1 rompión con su piedra a la tijera del " + \
                "Jugador 2 y gana la partida!"
            winner = 1
        else:
            message = "¡Oh, el Jugador 1 quiere tirar una piedra pero el " + \
                "Jugador 2 envuelve a su adversario con papel y gana esta partida!"
            winner = 2
    elif player_1 == "P":
        if player_2 == "R":
            message = "El Jugador 1 envuelve habilmente la piedra del Jugador " + \
                "2 y gana la partida rapidamente."
            winner = 1
        else:
            message = "El Jugador 1 quiere sacar papel pero es deborado por " + \
                "la tijera del Jugador 2, dejándolo papel picado."
            winner = 2
    elif player_1 == "T":
        if player_2 == "P":
            message = "Las tijeras del Jugador 1 arrasan con todo y se comen " + \
                "como pan caliente al papel del Jugador 2."
            winner = 1
        else:
            message = "El Jugador 1 arranca haciendose el machito con unas " + \
                "tijeras de morondanga y el Jugador 2 se las hace pelota de una pedrada."
            winner = 2
    else:
        message = "¡Oh no! Uno de los jugadores tiene artrosis en los dedos " + \
            "e ingresó una opción incorrecta."

    if winner != 0:
        message += f"\nEl  Jugador {winner} gana este round 🥊"
        if winner == 1:
            player_1_victories += 1
        else:
            player_2_victories += 1

    print("\n" + message)

    if player_1_victories == 3 or player_2_victories == 3:
        
        if player_1_victories == 3:
            winner = 1
        else:
            winner = 2

        break

print(f"\nFelicitaciones Jugador {winner} has ganado el juego. 🏆")
