#! python3

# Obtener el texto del portapapeles, agregar una estrella y un espacio 
# al comienzo de cada línea y luego pegar este nuevo texto en el portapapeles.

import pyperclip

texto = pyperclip.paste()

lista = texto.split("\n")
for indice, linea in enumerate(lista):
    lista[indice] = "* " + linea

texto = "\n".join(lista)
pyperclip.copy(texto)