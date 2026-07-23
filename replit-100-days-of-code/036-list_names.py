import os
import time
from mylib import input_color, color_me


def add_to_list(first_name: str, last_name: str):
    first_name = first_name.capitalize().strip()
    last_name = last_name.capitalize().strip()
    full_name = f"{first_name} {last_name}"
    if full_name in list_names:
        print(color_me("\nERROR: Nombre duplicado.\n", "red"))
    else:
        list_names.append(full_name)
        print_list()

    time.sleep(2)


def print_list():
    print("\nLista de nombres\n")
    for item in list_names:
        print("-", item)
    print()


list_names = []

while True:
    os.system("clear")

    print(color_me("*** Mis contactos ***\n", "yellow"))
    
    first_name = input_color("Nombre: ", color_input="green")
    last_name = input_color("Apellido: ", color_input="green")

    if first_name == "" or last_name == "":
        break

    add_to_list(first_name, last_name)
