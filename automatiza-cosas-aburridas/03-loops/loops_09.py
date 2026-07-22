"""
Usando el módulo sys para salir del bucle infinito y terminar el programa.
"""

import sys

while True:
    print("Escriba exit para salir del programa")
    response = input("> ")
    if response == "exit":
        sys.exit()
    print("Escribiste:", response)
