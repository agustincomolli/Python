"""
Escribir un programa que puede simular el funcionamiento de un display de 
siete segmentos, aunque vas a usar LEDs individuales en lugar de segmentos.

### ###
# # # #
### ###
# #   #
###   #

"""

from mylib import *

def print_number(number:str):
    """
    Imprime en la consola un número como si fuera un display de 7 segmentos.

    Args:
        number (str): Número entero positivo en formato string que será
                      mostrado en formato display.

    """

    digits = [
        ["###", "# #", "# #", "# #", "###"], # = 0
        ["  #", "  #", "  #", "  #", "  #"], # = 1
        ["###", "  #", "###", "#  ", "###"], # = 2
        ["###", "  #", "###", "  #", "###"], # = 3
        ["# #", "# #", "###", "  #", "  #"], # = 4
        ["###", "#  ", "###", "  #", "###"], # = 5
        ["###", "#  ", "###", "# #", "###"], # = 6
        ["###", "  #", "  #", "  #", "  #"], # = 7
        ["###", "# #", "###", "# #", "###"], # = 8
        ["###", "# #", "###", "  #", "  #"], # = 9
    ]

    # Convertir el número en una lista
    number_list = [int(digit) for digit in number]

    print()

    for row in range(5):
        line = ""
        for digit in number_list:
            line += digits[digit][row] + " "
        print(line)

    print()


def get_number() -> str:
    """
    Obtiene la entrada del usuario y valida que sea un número entero positivo

    """
    
    number = input_color("Ingrese un número: ", "green")
    try:
        if not number.isdigit() or int(number) < 0:
            raise ValueError("Ingrese un número entero positivo.")
        return number
    except ValueError as error:
        show_error(str(error))
        exit()


clear_screen()
print(color_me("Display para números\n", "yellow"))

number = get_number()
print_number(number)