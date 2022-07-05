#! python3

# Portapapeles múltiple.

# mcb.pyw: guarda y carga fragmentos de texto en el portapapeles.
# Uso: py.exe mcb.pyw guardar <palabra clave>: guarda el portapapeles como palabra clave.
# py.exe mcb.pyw <palabra clave>: carga la palabra clave en el portapapeles.
# py.exe mcb.pyw list: carga todas las palabras clave en el portapapeles.

import shelve, pyperclip, sys

datos_guardados = shelve.open("mcb")

# Guardar el contenido del portapapeles.
if len(sys.argv) == 3 and sys.argv[1].lower() == "guardar":
    datos_guardados[sys.argv[2]] = pyperclip.paste()
    print(list(datos_guardados.keys()))
elif len(sys.argv) == 3 and sys.argv[1].lower() == "borrar":
    datos_guardados.pop(sys.argv[2])
elif len(sys.argv) == 2:
    # Listar palabras claves y cargar el contenido.
    if sys.argv[1].lower() == "lista":
        pyperclip.copy(str(list(datos_guardados.keys())))
    elif sys.argv[1] in datos_guardados:
        pyperclip.copy(datos_guardados[sys.argv[1]])

datos_guardados.close()