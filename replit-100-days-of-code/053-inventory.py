from mylib import clear_screen, color_me, input_color, press_enter_to_continue
import time


def auto_save():
    """
        DESCRIPTION: Guarda la lista del inventario en un archivo.
    """

    file = open("./inventory.txt", mode="w", encoding="UTF-8")
    file.write(str(inventory))
    file.close()


def auto_load():
    """
        DESCRIPTION: Carga la lista del inventario previamente guardado.
    """

    try:
        file = open("./inventory.txt", mode="r", encoding="UTF-8")
        data = eval(file.read())
        file.close()
        return data
    except:
        print(color_me("ERROR: No se puede cargar el archivo " +
                       "'inventory.txt'.", "red"))
        press_enter_to_continue()
        return []


def add():
    """
        DESCRIPTION: Devuelve un item para agregar en la lista de inventario.
    """
    
    clear_screen()
    print(color_me("INVENTARIO 💼\n" + "=" * 13 + "\n", "yellow"))
    item = input_color("Ingrese el item a agregar: ", color_input="green")
    print(color_me("\nItem agregado", "blue"))
    time.sleep(3)
    return item.capitalize()


def view():
    """
        DESCRIPTION: Lista los items del inventario y su cantidad.
    """
    unique = []

    clear_screen()
    print(color_me("INVENTARIO 💼\n" + "=" * 13 + "\n", "yellow"))
    for item in inventory:
        if not item in unique:
            unique.append(item)

    unique.sort()
    
    for item in unique:
        print(f"{item}: {inventory.count(item)}")

    print()

    press_enter_to_continue()


def remove():
    """
        DESCRIPTION: Devuelve un item para agregar en la lista de inventario.
    """
    
    clear_screen()
    print(color_me("INVENTARIO 💼\n" + "=" * 13 + "\n", "yellow"))
    item = input_color("Ingrese el item a eliminar: ", color_input="green")
    print(color_me("\nItem eliminado", "blue"))
    time.sleep(3)
    return item.capitalize()


inventory = auto_load()
while True:
    clear_screen()
    print(color_me("INVENTARIO 💼\n" + "=" * 13 + "\n", "yellow"))

    print(" 1 - Agregar item")
    print(" 2 - Ver items")
    print(" 3 - Eliminar item")
    print(" 4 - Salir")

    option = input_color("\nElija una opción: ", color_input="green")

    if option == "1":
        inventory.append(add()) 
    elif option == "2":
        view()
    elif option == "3":
        inventory.remove(remove())
    elif option == "4":
        auto_save()
        break
    else:
        print(color_me("ERROR: Elija una opción válida.\n", "red"))
        press_enter_to_continue()
