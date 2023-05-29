"""
Tu tarea es escribir un programa que:

Pida al usuario el nombre del archivo de entrada.
- Lea el archivo (si es posible) y cuente todas las letras latinas (las letras 
mayúsculas y minúsculas se tratan como iguales).
- Imprima un histograma simple en orden alfabético (solo se deben presentar 
recuentos distintos de cero).

"""

from os import strerror

def make_histogram(file_name:str):
    """
    Crear un histograma con la cantidad de veces que aparecen cada letra del 
    abcdario en el archivo solicitado.

    Args:
        file_name(str): es el nombre del archivo a analizar.

    Return:
            Devuelve un diccionario con el histograma mostrando todas las 
            letras y la cantidad de veces que aparecen.

    """
    
    # Crear el diccionario.
    letters = {}
    for letter in range(ord("a"), ord("z")):
        letters[chr(letter)] = 0

    try:
        # Leer el archivo línea a línea y caracter por caracter.
        with open(file_name, mode="r", encoding="UTF-8") as file:
            for line in file.readlines():
                for char in line:
                    if char.lower() in letters:
                        letters[char.lower()] += 1
            
            return letters
    except IOError as file_error:
        print(f"\nNo se puede abrir el archivo: {strerror(file_error.errno)}")


file = input("Ingrese el nombre del archivo: ")

histogram = make_histogram(file)

print(histogram)