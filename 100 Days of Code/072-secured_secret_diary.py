from mylib import *
import getpass
import datetime
import hashlib
from time import sleep
from random import randint
import os


def add():
    """
    Description: Agrega una entrada en el diario usando el timestamp 
                 como clave.
    """

    clear_screen()
    print(color_me("📰 Diario secreto 🔒\n", "yellow"))
    entry = input_color("Escribe aquí 👉: ", color_input="green")
    diary[datetime.datetime.now()] = entry


def view():
    """
    Description: Muestra la última entrada del diario y pregunta si desea ver
                 la entrada anterior.
    """

    # Obtener todas las claves y ordenarlas para que la última ingresada sea
    # la primera de la lista.
    key_list = []
    for key in diary.keys():
        key_list.append(key)
    key_list.sort(reverse=True)

    index = 0
    view_next = "s"
    while view_next:
        clear_screen()
        print(color_me("📰 Diario secreto 🔒\n", "yellow"))

        # Verificar si hay datos para mostrar.
        if index > len(key_list) - 1:
            print("No hay más entradas en el diario.\n")
            press_enter_to_continue()
            return

        date = datetime.datetime.strftime(key_list[index], '%d-%m-%Y')
        time = datetime.datetime.strftime(key_list[index], '%H:%M:%S')
        print(f"Fecha: {date} - Hora: {time}\n")
        print(" - " + diary[key_list[index]])

        view_next = input_color("\n¿Ver siguiente? [s|n]: ",
                                color_input="green").lower()
        if view_next == "s":
            index += 1
        else:
            return


def login():
    with open("./secret.pass") as file:
        check_user = file.readline().strip()
        check_pass = file.readline().strip()
        check_salt = file.readline().strip()

    print(color_me("🌟 Iniciar Sesión 🌟\n"))
    username = input_color("Nombre de usuario: ", "green")
    password = getpass.getpass(color_me("Contraseña: ", ""))

    if username == check_user:
        hashed_pass = hashlib.sha256(f"{password}{check_salt}".encode())
        if hashed_pass.hexdigest() != check_pass:
            show_error("La contraseña no es correcta.")
            exit()
    else:
        show_error("El usuario no es el correcto.")
        exit()


def create_user():
    """
    Description: Crea el usuario para ingresar al programa.
    """

    print(color_me("👧 Crear nuevo usuario 🧑\n"))

    username = input_color("Nombre de usuario: ", "green")
    password = getpass.getpass(color_me("Contraseña: ", ""))
    # Fortalecer la contraseña.
    salt = randint(1000, 9999)
    password = f"{password}{salt}"
    # Encriptar la contraseña
    password = hashlib.sha256(password.encode())
    # Guardar los datos en un archivo.
    with open("./secret.pass", "w", encoding="UTF-8") as file:
        file.write(f"{username}\n")
        file.write(f"{password.hexdigest()}\n")
        file.write(f"{salt}")

    print(color_me("\nUsuario creado 👍\n", "blue"))
    sleep(3)
    clear_screen()
    exit()


diary = {}

clear_screen()
print(color_me("📰 Diario secreto 🔒\n", "yellow"))

# Si se inicia el programa por primera vez...
if not os.path.exists("./secret.pass"):
    create_user()
else:
    login()

while True:
    clear_screen()

    menu_title = color_me("📰 Diario secreto 🔒", "yellow")
    menu_options = ["Agregar", "Ver", "Salir"]
    choice = choose_option(menu_title, menu_options, "green")

    if choice == 1:
        add()
    elif choice == 2:
        view()
    else:
        break
