#!\\usr\\bin\\env python3

""" module.py - Un ejemplo de un módulo en Python. """

__contador = 0

def sumar_Lista(lista):
    global __contador
    __contador += 1
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

def producto_Lista(lista):
    global __contador   
    __contador += 1
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto

if __name__ == "__main__":
    print("Preferiría ser un módulo, pero puedo hacer unas pruebas para usted.")
    lst = [i+1 for i in range(5)]
    print(sumar_Lista(lst) == 15)
    print(producto_Lista(lst) == 120)