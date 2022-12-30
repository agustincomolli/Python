import tkinter as tk


def do_operation(number1: str, operator: str, number2: str):
    # Convertir los números en cadenas a formato de números con decimales.
    number1 = float(number1)
    number2 = float(number2)
    
    # Realizar la operación matemática de acuerdo al operador.
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        if number2 == 0:
            return "ERROR"
        result = number1 / number2

    # Si el resultado de la operación da un decimal 0, quedarse
    # con la parte entera...
    if float(result) % 1 == 0.0:
        result = int(result)

    return str(result)


def reset():
    # Reiniciar la calculador.

    global number_in_memory
    global operator
    global is_new_number

    result_label["text"] = "0"
    number_in_memory = None
    is_new_number = True
    operator = None


def button_pressed(value: str):
    global number_in_memory
    global operator
    global is_new_number

    # Si hay un error, reiniciar la calculadora.
    if result_label["text"] == "ERROR":
        reset()

    # Si presiona un número...
    if value.isdigit():
        # ¿Está ingresando un número nuevo?...
        if is_new_number:
            result_label["text"] = value
            is_new_number = False
        else:
            result_label["text"] += value
    # Si ingresa el punto y no está anteriormente ingresado...
    elif value == "." and value not in result_label["text"]:
        result_label["text"] += value
    # Si ingresa un operador matemático...
    elif value in ["+", "-", "*", "/"]:
        # ¿Si no hay un número en memoria?...
        if number_in_memory == None:
            # Guardar el número y habilitar el ingreso de un número nuevo.
            number_in_memory = result_label["text"]
            is_new_number = True
        else:
            # Realizar la operación matemática.
            number_in_memory = do_operation(
                number_in_memory, operator, result_label["text"])
            result_label["text"] = number_in_memory
            is_new_number = True
        # Guardo temporalmente el operador ingresado.
        operator = value
    elif value == "=":
        if number_in_memory != None:
            result_label["text"] = do_operation(
                number_in_memory, operator, result_label["text"])
            number_in_memory = None
            is_new_number = True
    else:
        reset()


def create_buttons():
    """
        Description: Crea los botones de la calculadora, a partir de un
                     diccionario que tiene el orden de los mismos.
                     Los botones +, = y 0 tiene el doble de tamaño y
                     ocupan mas filas o columnas según corresponda.
    """
    # Definir un diccionario con los valores de los botones.
    values = {
        "C": (1, 0), "/": (1, 1), "*": (1, 2), "-": (1, 3),
        "7": (2, 0), "8": (2, 1), "9": (2, 2), "+": (2, 3),
        "4": (3, 0), "5": (3, 1), "6": (3, 2),
        "1": (4, 0), "2": (4, 1), "3": (4, 2), "=": (4, 3),
        "0": (5, 0), ".": (5, 2)
    }

    # Crear los botones y posicionarlos.
    for value, position in values.items():
        if value == "+" or value == "=":
            # Los botones + e = tienen el doble de alto.
            button = tk.Button(frame, text=value, height=7, width=6)
            # Y ocupan dos filas.
            button.grid(row=position[0]+1, column=position[1], rowspan=2)
        elif value == "0":
            # El botón 0 tiene el doble de ancho.
            button = tk.Button(frame, text=value, height=3, width=14)
            # Y ocupa dos columnas.
            button.grid(row=position[0]+1, column=position[1], columnspan=2)
        else:
            button = tk.Button(frame, text=value, height=3, width=6)
            button.grid(row=position[0]+1, column=position[1])

        button.config(command=lambda v=value: button_pressed(v))


number_in_memory = None
operator = None
is_new_number = True
# Crear la ventana y establecer el título.
window = tk.Tk()
window.title("Calculadora")
window.geometry("240x350")

# Crear un contenedor para los controles y alinearlo al centro de la ventana.
frame = tk.Frame(window)
frame.place(relx=.5, rely=.5, anchor="center")

# Crea la etiqueta para mostrar el resultado.
# anchor="e" alinea la etiqueta hacia la derecha.
result_label = tk.Label(frame, text="0",  font="Helvetica 11 bold", width=21,
                        borderwidth=1, relief="solid", background="white",
                        anchor="e", padx=10, pady=4)
result_label.grid(row=0, column=0, columnspan=4, pady=(4, 8))

# Crear los botones de la calculadora.
create_buttons()
# Ejecutar el programa.
tk.mainloop()
