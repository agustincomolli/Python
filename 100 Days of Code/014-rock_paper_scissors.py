from getpass import getpass as input

print("*** Batalla 🪨 📄✂️  Epica ***")

print("\nElija una opción 🪨  = R, 📄 = P, ✂️  = T\n")

player_1 = input("Jugador 1: ").upper()
player_2 = input("Jugador 2: ").upper()

if player_1 == player_2:
    message = "¡Empate!"
    winner = 0
elif player_1 == "R":
    if player_2 == "T":
        message = "¡El jugador 1 rompión con su piedra a la tijera del jugador 2 y gana la partida!"
        winner = 1
    else:
        message = "¡Oh, el jugador 1 quiere tirar una piedra pero el jugador 2 envuelve a su adversario con papel y gana esta partida!"
        winner = 2
elif player_1 == "P":
    if player_2 == "R":
        message = "El jugador 1 envuelve habilmente la piedra del jugador 2 y gana la partida rapidamente."
        winner = 1
    else:
        message = "El jugador 1 quiere sacar papel pero es deborado por la tijera del jugador 2, dejándolo papel picado."
        winner = 2
elif player_1 == "T":
    if player_2 == "P":
        message = "Las tijeras del jugador 1 arrasan con todo y se comen como pan caliente al papel del jugador 2."
        winner = 1
    else:
        message = "El jugador 1 arranca haciendose el machito con unas tijeras de morondanga y el jugador 2 se las hace pelota de una pedrada."
        winner = 2
else:
    message = "¡Oh no! Uno de los jugadores tiene artrosis en los dedos e ingresó una opción incorrecta."

if winner != 0:
    message += f"\nFelicitaciones Jugador {winner} has ganado el juego. 🏆"
    
print("\n" + message)