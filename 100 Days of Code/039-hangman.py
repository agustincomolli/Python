import random
from mylib import color_me, input_color, clear_screen

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

hardware_list = ["monitor", "teclado", "mouse", "procesador", "ram",
                 "disco", "pendrive", "impresora", "webcam", "motherboard"]

random_word = random.choice(hardware_list)
hidden_word = ["_"] * len(random_word)
lives = len(HANGMAN_PICS) - 1


def show_interface():
    """
        DESCRIPTION: Muestra la pantalla del juego.

    """

    clear_screen()
    print(color_me("*** AHORCADO ***\n", "yellow"))
    # Vidas restantes.
    print(color_me(f"Vidas: {'❤️' * lives}", "red"))
    # Dibujo del ahorcado.
    print(HANGMAN_PICS[len(HANGMAN_PICS) - lives - 1])
    # Mostrar la cantidad de caracteres de la palabra elegida.
    print()
    for letter in hidden_word:
        print(letter + " ", end="")
    print()


while True:
    show_interface()
    
    # Chequear si perdió.
    if lives == 0:
        print(color_me("\n¡PERDISTE! El juego ha terminado ☠️", "red"))
        print(f"\nLa palabra era: {random_word}\n")
        break
    
    # Chequear si ganó.
    if not "_" in hidden_word:
        print(color_me("\n¡GANASTE! Felicitaciones has acertado con " +
                       "la palabra 🥳\n", "blue"))
        break
    
    current_letter = input_color(
        "\nElige una letra: ", color_input="green").upper()
    found_letter = False

    for i in range(len(random_word)):
        if random_word[i].upper() == current_letter:
            hidden_word[i] = current_letter
            found_letter = True

    if not found_letter:
        lives -= 1
