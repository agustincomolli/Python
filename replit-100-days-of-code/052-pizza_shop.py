from mylib import clear_screen, color_me, input_color, press_enter_to_continue
import time


def auto_load():
    """
        DESCRIPTION: Carga los pedidos guardados con anterioridad y 
                     devuelve una lista.
    """

    try:
        file = open("./pizzas_order.txt", mode="r", encoding="UTF-8")
        data = eval(file.read())
        file.close()
        return data
    except Exception:
        print(color_me("ERROR: No se puede cargar 'pizzas_order.txt'", "red"))
        press_enter_to_continue()
        return []


def auto_save():
    """
        DESCRIPTION: Guarda la lista de pedidos en un archivo.
    """

    file = open("./pizzas_order.txt", mode="w", encoding="UTF-8")
    # Convertir la lista en texto y grabar en el archivo.
    file.write(str(orders))
    file.close()


def add():
    """
        DESCRIPTION: Agrega un pedido y devuelve una lista con un solo pedido.
    """

    clear_screen()

    print(color_me("La Pizza di Comolli 🍕\n", "yellow"))

    name = input_color("Nombre: ", color_input="green")
    pizza = input_color("Pizza: ", color_input="green")
    size = input_color("Tamaño (c,m,g): ", color_input="green").lower()
    if size == "c":
        cost = 5.99
    elif size == "m":
        cost = 9.99
    elif size == "g":
        cost = 15.99
    quantity = input_color("Cantidad: ", color_input="green")
    try:
        quantity = int(quantity)
    except:
        print(color_me("ERROR. Cantidad debe ser un número entero.\n", "red"))
        press_enter_to_continue()
        return []
    total = quantity * cost

    return [name, pizza, size, quantity, total]


def view():
    """
        DESCRIPTION: Muestra la lista de pedidos en la pantalla.
    """

    clear_screen()

    print(color_me("La Pizza di Comolli 🍕\n", "yellow"))
    print("Lista de pedidos:")
    print(color_me(f"\n{'Nombre':^20}   {'Pizza':^20}   {'Tamaño':^10}   " +
                   f"{'Cantidad':^10}   {'Total':^10}", "blue"))
    for row in range(len(orders)):
        print(
            f"{orders[row][0]:^20} | {orders[row][1]:^20} | " +
            f"{orders[row][2]:^10} | {orders[row][3]:^10} | " +
            f"{'$ ' + str(orders[row][4]):^10}")
    press_enter_to_continue()


# Cargar pedidos anteriores.
orders = auto_load()
while True:
    clear_screen()

    print(color_me("La Pizza di Comolli 🍕\n", "yellow"))

    print("1 - Agregar pizza\n2 - Ver pizzas\n3 - Salir\n")
    option = input_color("Elija una opción: ", color_input="green")

    if option == "1":
        orders.append(add())
    elif option == "2":
        view()
    elif option == "3":
        # Guardar pedidos y salir del programa.
        auto_save()
        break
    else:
        print(color_me("\nError. El valor ingresado no es válido.", "red"))
        time.sleep(3)
