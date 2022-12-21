from mylib import choose_option, clear_screen, color_me, input_color
from mylib import press_enter_to_continue
import getpass
import datetime


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

diary = {}

clear_screen()
print(color_me("📰 Diario secreto 🔒\n", "yellow"))

# Pedir contraseña de acceso al programa.
password = getpass.getpass("Ingrese la contraseña de entrada: ")
if password != "pass":
    print(color_me("\nERROR: Contraseña inválida.", "red"))
    exit()

while True:
    clear_screen()

    menu_title = color_me("📰 Diario secreto 🔒", "yellow")
    menu_options = ["Agregar", "Ver", "Salir"]
    choice = choose_option(menu_title, menu_options)

    if choice == 1:
        add()
    elif choice == 2:
        view()
    else:
        break
