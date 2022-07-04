#! python3

# Portapapeles múltiple.

# mcb.pyw: guarda y carga fragmentos de texto en el portapapeles.
# Uso: py.exe mcb.pyw guardar <palabra clave>: guarda el portapapeles como palabra clave.
# py.exe mcb.pyw <palabra clave>: carga la palabra clave en el portapapeles.
# py.exe mcb.pyw list: carga todas las palabras clave en el portapapeles.

import shelve, pyperclip, sys

datos_guardados = shelve.open("mcb")



datos_guardados.close()