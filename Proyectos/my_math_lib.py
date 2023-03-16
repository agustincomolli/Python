def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
    radio (float): radio del círculo.

    Returns:
    float: área del círculo.
    """
    return 3.14 * radio * radio


def convertir_celsius_a_fahrenheit(grados_celsius):
    """
    Convierte grados Celsius a Fahrenheit.

    Args:
    grados_celsius (float): grados Celsius a convertir.

    Returns:
    float: grados Fahrenheit.
    """
    return (grados_celsius * 1.8) + 32


def calcular_factorial(numero):
    """
    Calcula el factorial de un número dado.

    Args:
    numero (int): número del cual se desea calcular el factorial.

    Returns:
    int: factorial del número.
    """
    # Inicializamos el factorial en 1
    factorial = 1
    # Iteramos desde 1 hasta el número dado
    for i in range(1, numero+1):
        # Multiplicamos el factorial por el número actual
        factorial = factorial * i
    # Devolvemos el factorial
    return factorial


def es_numero_primo(numero):
    """
    Verifica si un número es primo.

    Args:
    numero (int): número a verificar.

    Returns:
    bool: True si el número es primo, False en caso contrario.
    """
    # Si el número es menor que 2, entonces no es primo
    if numero < 2:
        return False
    # Iteramos desde 2 hasta el número dado
    for i in range(2, numero):
        # Si el número es divisible por algún número en este rango, entonces no es primo
        if numero % i == 0:
            return False
    # Si no se ha encontrado un número que lo divida, entonces es primo
    return True


def encontrar_mcd(num1, num2):
    """
    Encuentra el máximo común divisor (MCD) de dos números.

    Args:
    num1 (int): primer número.
    num2 (int): segundo número.

    Returns:
    int: MCD de los dos números.
    """
    # Si alguno de los números es 0, el MCD es el otro número
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1

    # Asignamos a m el número mayor y a n el número menor
    if num1 > num2:
        m = num1
        n = num2
    else:
        m = num2
        n = num1

    # Iteramos hasta encontrar el MCD
    while m % n != 0:
        m, n = n, m % n

    # Devolvemos el MCD
    return n


def es_palindroma(cadena):
    """
    Verifica si una cadena es palíndroma.

    Args:
    cadena (str): cadena a verificar.

    Returns:
    bool: True si la cadena es palíndroma, False en caso contrario.
    """
    # Convertimos la cadena a minúsculas y eliminamos espacios en blanco
    cadena = cadena.lower().strip()
    # Invertimos la cadena y comparamos con la original
    return cadena == cadena[::-1]
