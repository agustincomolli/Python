import random
import os

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


def print_title(key:str):
    """
        DESCRIPTION: Leer el archivo con el título en ASCII ART.
    """
    title = """"""

    try:
        with open(f"./{key}.txt", mode="r") as file:
            for line in file:
                title += line
    except FileNotFoundError:
        print(f"ERROR: archivo {key}.txt no encontrado")

    print(title)


def read_file():
    """
        DESCRIPTION: Leer el archivo con palabras para adivinar en el juego y
                     generar una lista.
    """
    word_list = []

    with open("./data.txt", mode="r", encoding="UTF-8") as file:
        for line in file:
            word_list.append(line.strip())
    
    return word_list


def get_random_word():
    """
        DESCRIPTION: Devuelve una palabra al azar de la lista de palabras.
    """
    word_list = read_file()

    return str(random.choice(word_list)).upper()


def clear_screen():
    """
        DESCRIPTION: Limpiar la pantalla según el sistena operativo.
                     posix = Linux o MAC
    """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def show_interface(hidden_word:str, tries:int):
    """
        DESCRIPTION: Muestra la pantalla del juego según el estado del mismo.
    """

    clear_screen()
    print_title("title")
    print(HANGMAN_PICS[tries])
    print("\n", hidden_word)


def run():
    word = get_random_word() 
    hidden_word = ["_"] * len(word)
    tries = 0

    while True:
        show_interface(hidden_word, tries)
        current_letter = input("\nElige una letra: ").upper()
        is_found = False

        # Buscar la letra en toda la palabra.
        for i in range(len(word)):
            if word[i] == current_letter:
                is_found = True
                hidden_word[i] = current_letter

        if not is_found:
            tries += 1
        
        if tries == (len(HANGMAN_PICS) - 1):
            show_interface(hidden_word, tries)
            print_title("lose")
            print(f"\nLa palabra era {word}")
            break
        elif not "_" in hidden_word:
            show_interface(hidden_word, tries)
            print_title("win")
            print(f"\nLa palabra era {word}")
            break

if __name__ == "__main__":
    run()
