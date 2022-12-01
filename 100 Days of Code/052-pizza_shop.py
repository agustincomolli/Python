from mylib import clear_screen, color_me, input_color, press_enter_to_continue
import time


def auto_load():
    pass


def auto_save():
    pass


def add():
    clear_screen()
    
    print(color_me("La Pizza di Comolli 🍕\n", "yellow"))
    name = input_color("Nombre: ", color_input="green")
    pizza = input_color("Pizza: ", color_input="green")
    size = input_color("Tamaño (c,m,g): ", color_input="green")
    quantity = input_color("Cantidad: ", color_input="green")

    return [name, pizza, size, quantity]

def view():
    print(orders)
    press_enter_to_continue()

orders = []
auto_load()
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
        auto_save()
        break
    else:
        print(color_me("\nError. El valor ingresado no es válido.", "red"))
        time.sleep(3)
