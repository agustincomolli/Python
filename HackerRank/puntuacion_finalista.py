#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input("Ingrese n: "))
    arr = map(int, input("Ingrese una lista de números separados por espacios: ").split())

    lista_ordenada = sorted([numero for numero in arr][:n])
    maximo = 0
    subcampeon = 0
    for numero in lista_ordenada:
        if maximo < numero:
            subcampeon = maximo
            maximo = numero
    print("El subcampeón es", subcampeon)    