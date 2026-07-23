"""
Conjetura de Collatz:
La conjetura establece que, si tomas cualquier número entero positivo y lo 
sigues iterando según la siguiente regla:

Si el número es par, divídelo por 2.
Si el número es impar, multiplícalo por 3 y añade 1.

Entonces, eventualmente, siempre terminarás en el número 1.
"""

print("*** Conjetura de Collatz ***\n")
number = int(input("Ingrese un número mayor a 1: "))

if number < 1:
    print("El número no cumple con la consigna.")
    exit()

steps = 0
while number != 1:
    # Si el número es par...
    if number % 2 == 0:
        # dividirlo por 2
        number /= 2
    else:
        # Si es impar, multiplicarlo por 3 y sumarle 1
        number = (number * 3) + 1
    
    steps += 1
    print(int(number))

print(f"Pasos = {steps}")