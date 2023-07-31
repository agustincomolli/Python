# Crear una función que genere números primos hasta el número dado por parámetro.
def generate_primes(number: int) -> list:
    """
    Genera un lista de números primos desde 1 hasta number.

    Retorna:
        list: Lista de números primos.
    """
    if number < 2:
        return []

    # Agregar el 2 a la lista porque es número primo.
    primes_list = [2]
    # Recorrer los números desde el 3 hasta el número inclusive, evitando
    # los números pares que no son primos
    for i in range(3, number + 1, 2):
        if is_prime(i):
            primes_list.append(i)

    return primes_list


def is_prime(number: int) -> bool:
    """
    Chequea si un número es primo o no.

    Retorna:
        bool: Devuelve True si es número primo.
    """

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    number = int(input("Ingrese un número: "))
    if number < 2:
        print("Debe ingresar un número mayor a 1.")
    else:
        primes_numbers = generate_primes(number)
        print(f"Los números primos generados son:\n{primes_numbers}")
        # print(f"¿{number} es primo? {is_prime(number)}")
