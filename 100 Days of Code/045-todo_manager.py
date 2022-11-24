from mylib import color_me, clear_screen, input_color
from mylib import press_enter_to_continue
import time

todo_list = []


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
    print(color_me("*** Administrador de Tareas ✔️ ***\n", "yellow"))
    print(text_option)

    option = input_color("Ingrese su opción: 👉 ", color_input="green")
    # Si lo ingresado no es número devolver 0
    if not option.isnumeric():
        option = 0
    
    return int(option)


def show_view_menu():
    """
        DESCRIPTION: Muestra el menú Ver.

    """

    text_option = "1 - Ver todas las tareas\n"
    text_option += "2 - Ver tareas por prioridad\n"
    text_option += "3 - Volver\n\n\n"

    clear_screen()
    print(color_me("*** Menú Ver ***\n", "yellow"))
    print(text_option)

    option = input_color("Ingrese su opción: 👉 ", color_input="green")
    # Si lo ingresado no es número devolver 0.
    if not option.isnumeric():
        option = 0
    else:
        option = int(option)

    if option == 1:
        view(False)
    elif option == 2:
        view(True)
    elif option == 3:
        return
    else:
        print(color_me("\nERROR: Opción inválida. Intente de nuevo.", "red"))
        time.sleep(3)
        return


def add():
    """
        DESCRIPTION: Agrega una tarea nueva.

    """
    clear_screen()
    print(color_me("Agregar una tarea\n", "yellow"))
    
    task = input_color("Tarea: ", color_input="green").lower()
    date = input_color("Fecha: ", color_input="green").lower()
    priority = input_color("Prioridad: ", color_input="green").lower()

    todo_list.append([task, date, priority])
    print(color_me("\nTarea agregada.", "blue"))
    time.sleep(2)
    

def view(has_priority: bool):
    """
        DESCRIPTION: Muestra las tareas.
        PARAMETERS: 
                     has_priority: indica si se ven todas las tareas o solo
                     las que tienen prioridad.

    """
    clear_screen()
    print(color_me("Ver tareas\n", "yellow"))

    if has_priority:
        for row in todo_list:
            if row[2] == "alta":
                print(f"{row[0]:<30}\t | {row[1]:^10} | \t{row[2]:<10}")
    else:
        for row in todo_list:
            print(f"{row[0]:<30}\t | {row[1]:^10} | \t{row[2]:<10}")

    print()
    press_enter_to_continue()


def edit():
    """
        DESCRIPTION: Modificar una tarea determinada.

    """
    clear_screen()
    print(color_me("Editar una tarea\n", "yellow"))

    task = input_color("¿Qué tarea desea editar? ", color_input="green")

    is_found = False

    for idx in range(len(todo_list)):
        if task == todo_list[idx][0]:
            task = input_color("Nueva tarea: ", color_input="green")
            date = input_color("Neva fecha: ", color_input="green")
            priority = input_color("Nueva prioridad: ", color_input="green")
            todo_list[idx][0] = task.lower()
            todo_list[idx][1] = date.lower()
            todo_list[idx][2] = priority.lower()
            is_found = True
            break

    if is_found:
        print(color_me("\nTarea modificada", "blue"))
    else:
        print(color_me("\nERROR: Esa tarea no existe en la lista", "red"))

    time.sleep(2)


def delete():
    """
        DESCRIPTION: Eliminar una tarea determinada.

    """
    clear_screen()
    print(color_me("Eliminar una tarea\n", "yellow"))

    task = input_color("¿Qué tarea desea eliminar? ", color_input="green")

    if task == "todas":
        todo_list = []
        return
    
    is_found = False

    for idx in range(len(todo_list)):
        if task == todo_list[idx][0]:
            todo_list.pop(idx)
            is_found = True
            break

    if is_found:
        print(color_me("\nTarea eliminada", "blue"))
    else:
        print(color_me("\nERROR: Esa tarea no existe en la lista", "red"))

    time.sleep(2)


while True:
    option = show_menu()
    if option == 1:
        add()
    elif option == 2:
        show_view_menu()
    elif option == 3:
        edit()
    elif option == 4:
        delete()
    elif option == 5:
        break
    else:
        print(color_me("\nERROR: Opción inválida. Intente de nuevo.", "red"))
        time.sleep(3)
