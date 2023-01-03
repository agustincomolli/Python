import tkinter as tk


def restart_game():
    """
    Description: Reinicia el juego.
    """
    window.destroy()
    start_game()


def change_image():
    """
        Description: En base a la entrada del usuario y de la imagen que
                     se muestra, ir cambiando la imagen hasta ganar la
                     partida. Si no mostrar un mensaje de que perdió.
    """
    global image

    text = textbox.get().lower()
    image_name = image.cget("file")

    if text == "perro" and image_name == "./guess_who/dog.png":
        image = tk.PhotoImage(file="./guess_who/cat.png")
        canvas.itemconfig(container, image=image)
    elif text == "gato" and image_name == "./guess_who/cat.png":
        image = tk.PhotoImage(file="./guess_who/chicken.png")
        canvas.itemconfig(container, image=image)
    elif text == "gallina" and image_name == "./guess_who/chicken.png":
        image = tk.PhotoImage(file="./guess_who/bunny.png")
        canvas.itemconfig(container, image=image)
    elif text == "conejo" and image_name == "./guess_who/bunny.png":
        image = tk.PhotoImage(file="./guess_who/monkey.png")
        canvas.itemconfig(container, image=image)
    elif text == "mono" and image_name == "./guess_who/monkey.png":
        image = tk.PhotoImage(file="./guess_who/panda.png")
        canvas.itemconfig(container, image=image)
    elif text == "oso panda" and image_name == "./guess_who/panda.png":
        # Eliminar el objeto canvas con los objetos que contiene.
        canvas.destroy()
        # Mostrar etiqueta que ganó
        new_label = tk.Label(
            text="¡Ganaste!", foreground="blue", font=("Helvetica", 20, "bold"))
        new_label.grid(row=3, column=0, pady=(80))
        # Deshabilitar el botón.
        find_button["state"] = "disabled"
        # Crear botón para reiniciar el juego.
        restart_button = tk.Button(text="Reiniciar", width=10,
                                   height=2, command=restart_game)
        restart_button.grid(row=4, column=0, pady=(10, 5))
    else:
        # Eliminar el objeto canvas con los objetos que contiene.
        canvas.destroy()
        # Mostrar etiqueta que perdió
        new_label = tk.Label(
            text="¡Perdiste!", foreground="red", font=("Helvetica", 20, "bold"))
        new_label.grid(row=3, column=0, pady=(80))
        # Deshabilitar el botón.
        find_button["state"] = "disabled"
        # Crear botón para reiniciar el juego.
        restart_button = tk.Button(text="Reiniciar", width=10,
                                   height=2, command=restart_game)
        restart_button.grid(row=4, column=0, pady=(10, 5))


def create_game_widgets(window: tk.Tk):
    # Crear el título.
    title = tk.Label(text="¿Quién es Quién?", foreground="darkcyan",
                     font=("Helvetica", 14, "bold"))
    title.grid(row=0, column=0, pady=10)

    # Crear la caja de texto.
    textbox = tk.Entry(window, font=("Helvetica", 11), width=40)
    textbox.grid(row=1, column=0)

    # Crear botón
    find_button = tk.Button(text="Buscar", width=10,
                            height=2, command=change_image)
    find_button.grid(row=2, column=0, pady=(10, 5))

    # Crear canvas.
    canvas = tk.Canvas(window, width=350, height=300)
    canvas.grid(row=3, column=0, pady=10)

    # Crear imagen.
    image = tk.PhotoImage(file="./guess_who/dog.png")
    container = canvas.create_image(175, 100, image=image)

    return textbox, find_button, canvas, image, container


def create_window():
    # Crear la ventana.
    new_window = tk.Tk()
    new_window.title("¿Quién es Quién?")
    # Centrar en la pantalla.
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    window_width = 400
    window_height = 400
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    new_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Hacer que la columna 0 ocupe todo el ancho de la grilla
    # para poder centrar los elementos de la ventana.
    new_window.grid_columnconfigure(0, weight=1)

    return new_window


def start_game():
    """
    Description: Crea la ventana, y los controles del juego e inicia el 
                 programa.
    """

    global window
    global textbox, find_button, canvas, image, container

    window = create_window()
    textbox, find_button, canvas, image, container = create_game_widgets(
        window)

    # Ejecutar el programa.
    tk.mainloop()


start_game()
