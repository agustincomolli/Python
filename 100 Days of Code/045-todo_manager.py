from mylib import color_me, clear_screen, input_color
import time


def show_menu():
    """
        DESCRIPTION: Muestra el menú principal y devuelve la opción elegida.

    """

    text_option = "1 - Agregar\n"
    text_option += "2 - Ver\n"
    text_option += "3 - Editar\n"
    text_option += "4 - Eliminar\n"
    text_option += "5 - Salir\n"

    clear_screen()
    print(color_me("*** Administrador de Tareas ***\n", "yellow"))
    print(text_option)
    
    return int(input_color("Ingrese su opción: ", color_input="green"))


while True:
    option = show_menu()
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        break
    else:
        print(color_me("ERROR: Opción inválida. Intente de nuevo.", "red"))
        time.sleep(3)
