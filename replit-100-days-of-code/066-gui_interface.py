import tkinter as tk


def update_label():
    global number
    number += 1
    label_text = text.get("1.0", "end")
    label["text"] = f"{number} - {label_text}".strip()


# Crear una ventana nueva.
window = tk.Tk()
# Establecer el texto de la barra de título.
window.title("¡Hola mundo!")
# Establecer el tamaño inicial de la ventana.
window.geometry("640x480")

# Crear una etiqueta
label_text = "Esto ha sido hecho con TKinter"
label = tk.Label(text=label_text, foreground="green", font=("Arial", 14, "bold"))
# Colocar la etiqueta en la ventana.
label.grid(row=0, column=1)

# Crear una caja de texto.
text = tk.Text(width=30, height=1, font="Arial 11")
text.grid(row=1, column=1)

# Crear un botón.
button = tk.Button(text="Hazme clic 😎", width=15, height=2,
                   font=14, command=update_label)
# Colocar el botón en la ventana.
button.grid(row=2, column=1)
number = 0

tk.mainloop()
