"""
Serie Fibonacci:
Son una secuencia de números enteros los cuales siguen una regla sencilla:

El primer elemento de la secuencia es igual a uno (Fib1 = 1).
El segundo elemento también es igual a uno (Fib2 = 1).
Cada número después de ellos son la suman de los dos números anteriores 
(Fibi = Fibi-1 + Fibi-2).
"""

def fibonacci(num):
    if num < 1:
        return None
    elif num < 2:
        return 1
    
    fib_1 = fib_2 = 1
    the_sum = 0
    
    for i in range(3, num + 1):
        the_sum = fib_1 + fib_2
        fib_1, fib_2 = fib_2, the_sum

    return the_sum


for n in range(1, 10):  # probando
    print(n, "->", fibonacci(n))