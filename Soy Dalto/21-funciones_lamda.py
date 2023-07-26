# Funciones lamda:
function_name = lambda parameter: parameter * 2
#       |          |       |         |-> expresión de la función
#       |          |       |-> nombre del parámetro
#       |          |-> palabra reservada
#       |-> nombre de la función


double = lambda number: number * 2

print(f"El doble de 4 es: {double(4)}")
print(f"El doble de 73 es: {double(73)}")


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Usando un función normal...


def is_even(number: int) -> bool:
    """
    Verifica si un número dado es par.

    Parámetros:
        número (int): El número a verificar.

    Retorna:
        bool: True si el número es par, False de lo contrario.
    """
    if number % 2 == 0:
        return True
    

even_numbers = filter(is_even, numbers)
even_numbers = list(even_numbers)
print(f"Los números pares son: {even_numbers}")

# Usando una función lamda...
even_numbers = filter(lambda number: number % 2 == 0, numbers)
even_numbers = list(even_numbers)
print("\nUsando una función lamda:")
print(f"Los números pares son: {even_numbers}")

# Crear una función lamda que reciba un nombre e imprima un saludo.
greet = lambda name: print(f"¡Hola, {name}!")
greet("Agustín")