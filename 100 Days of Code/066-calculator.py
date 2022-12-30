import tkinter as tk


def button_pressed(value: str):
    global number_in_memory
    global operator
    global is_new_number

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
        # ¿No hay ningún número en memoria?...
        if number_in_memory == None:
            number_in_memory = result_label["text"]
            is_new_number = True
        else:
            # Evaluar la operación y mostrar el resultado.
            result = eval(number_in_memory + operator + result_label["text"])
            # Si el resultado de la operación da un decimal 0, quedarse
            # con la parte entera...
            if float(result) % 1 == 0.0:
                result = int(result)
            number_in_memory = str(result)
            result_label["text"] = number_in_memory
            is_new_number = True
        # Guardo temporalmente el operador ingresado.
        operator = value
    elif value == "=":
        if number_in_memory != None:
            # Evaluar la operación y mostrar el resultado.
            result = eval(number_in_memory + operator + result_label["text"])
            # Si el resultado de la operación da un decimal 0, quedarse
            # con la parte entera...
            if float(result) % 1 == 0.0:
                result = int(result)
            result_label["text"] = str(result)
            number_in_memory = None
            is_new_number = True
    else:
        # Si presiona el botón "C", resetear la calculadora.
        result_label["text"] = "0"
        number_in_memory = None
        is_new_number = True


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
