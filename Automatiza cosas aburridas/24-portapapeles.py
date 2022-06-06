#! python3
# portapapeles.py - Un programa multiportapapeles.

import sys
import pyperclip

texto = {
    "acuerdo": "Sí, estoy de acuerdo. Eso me parece bien.",
    "ocupado": "Lo siento, ¿podemos hacer esto más tarde esta semana o la próxima?",
    "adios": "Muchas gracias por su atención.\nSaluda atte.\nAgustín Comolli"
    }

if len(sys.argv) < 2:
    print("Uso: python 24-portapapeles.py [frase-clave] - copiar texto de frase.")
    sys.exit()

clave = sys.argv[1] # El primer argumento de la línea de comando es la clave.
if clave in texto:
    pyperclip.copy(texto[clave])
    print(f"Texto para '{clave} copiado al portapapeles.")
else:
    print(f"No hay texto para la clave {clave}.")