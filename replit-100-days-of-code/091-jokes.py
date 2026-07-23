import requests
from mylib import *


def new_joke():
    """
    Description: Devuelve un chiste en inglés usando una API
    """
    
    results = requests.get("https://icanhazdadjoke.com/",
                           headers={"Accept": "application/json"})
    joke = results.json()

    clear_screen()
    print(title)
    print(color_me(f"\n{joke['joke']}\n", "blue"))
    press_enter_to_continue()

    return joke["joke"]


def save_joke(last_joke:str):
    """
    Description: Guarda el último chiste en un archivo de texto.
    """

    clear_screen()
    print(title + "\n")

    if last_joke == "":
        print(color_me("No hay nada para guardar\n", "magenta"))
        press_enter_to_continue()
    else:
        with open("./jokes.txt", mode="a", encoding="UTF-8") as file:
            file.write(last_joke.strip() + "\n")
        print(color_me("Chiste guardado...\n", "blue"))
        press_enter_to_continue()


def load_jokes():
    """
    Description: Carga el archivo con todos los chistes guardados y muestra
                 los 10 últimos.
    """

    with open("./jokes.txt", mode="r", encoding="UTF-8") as file:
        jokes = file.readlines()

    jokes = jokes[::-1]

    clear_screen()
    print(title + "\n")

    if len(jokes) > 10:
        final = 10
    else:
        final = len(jokes)

    for i in range(final):
        print(f"{i + 1} - {jokes[i].strip()}")

    print()
    press_enter_to_continue()
    

title = color_me("Chistes en inglés API", "yellow")
menu = ["Nuevo chiste", "Guardar chiste", "Cargar chiste aleatorio", "Salir"]
last_joke = ""

while True:
    clear_screen()
    option = choose_option(title, menu, "green")

    if option == 1:
        last_joke = new_joke()
    elif option == 2:
        save_joke(last_joke)
    elif option == 3:
        load_jokes()
    elif option == 4:
        break
