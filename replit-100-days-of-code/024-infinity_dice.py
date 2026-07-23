def roll_dice(sides):
    import random

    rolled = random.randint(1, sides)
    print(f"Has sacado {rolled}")


print("*** Dado Infinito ***\n")
sides = int(input("¿Cuántas caras tiene tu dado 🎲? "))

while True:

    roll_dice(sides)

    roll_again = input("¿Desea tirar de nuevo? [s|n] ")
    if roll_again == "s":
        continue
    elif roll_again == "n":
        break
    else:
        print("No entendí tu respuesta.")
        exit()

print("\nGracias por jugar")