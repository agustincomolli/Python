"""
Recursividad:
La serie de Fibonacci es un claro ejemplo de recursividad. Ya te dijimos que:

Fibi = Fibi-1 + Fibi-2

"""

def fibonacci(num):
    if num < 1:
        return None
    elif num < 3:
        return 1
    
    return fibonacci(num - 1) + fibonacci(num - 2)


def factorial(num:int):
    # El caso base (condición de terminación).
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num


for n in range(1, 10):  # probando
    print(n, "->", fibonacci(n))
    
for num in range(1, 6):  # probando
    print(num, factorial(num))