# Crear una función que devuelva la serie de Fibonacci hasta el número dado.
def generate_fibonacci(number: int) -> list:
    """
    Genera una lista de números de la serie Fibonacci desde 1 hasta number.

    Retorna:
        list: La lista de números Fibonacci generados.
    """
    previous = 0
    current = 1
    number_list = [previous, current]
    while current + previous <= number:
        next = current + previous
        number_list.append(next)
        previous = current
        current = next

    return number_list


if __name__ == "__main__":
    stop_number = int(input("Ingrese un número: "))
    fibonacci_list = generate_fibonacci(stop_number)
    print(f"La lista de números Fibonacci es:\n{fibonacci_list}")
