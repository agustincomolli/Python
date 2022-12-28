import tkinter as tk


def button_pressed(value: str):
    if value.isdigit():
        if result_label["text"] == "0":
            result_label["text"] = value
        else:
            result_label["text"] += value

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


result = 0
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
