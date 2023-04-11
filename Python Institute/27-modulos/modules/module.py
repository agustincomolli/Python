#!/usr/bin/env python3

"""
Ejemplo de módulo en Python

"""

__counter = 0


def sum_list(the_list:list) -> int:
    global __counter
    __counter += 1
    the_sum = 0

    for element in the_list:
        the_sum += element

    return the_sum


def product_list(the_list:list) -> int:
    global __counter
    __counter += 1
    the_product = 1

    for element in the_list:
        the_product *= element

    return the_product


if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero puedo  realizar algunas pruebas.")
    my_list = [i + 1 for i in range(5)]
    print("¿La suma da 15?", sum_list(my_list) == 15)
    print("¿La multiplicación da 120?", product_list(my_list) == 120)