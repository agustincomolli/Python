"""
Factorial: es igual al producto de todos los números naturales previos 
al argumento o número dado.
"""

def factorial(num:int):
    """
    Description: Devuelve el factorial de un número.
    """
    
    if num <= 0:
        return None
    elif num == 1:
        return 1
    
    product = 1
    for i in range(2, num + 1):
        product *= i

    return product


for num in range(1, 6):  # probando
    print(num, factorial(num))
