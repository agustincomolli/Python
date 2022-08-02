# Convertir números decimales en binarios.

def decimal_to_binary(decimal_number:int) -> int:
    """
        DESCRIPTION: Convierte un número decimal en binario.
        PARAMETERS: decimal_number = número entero decimal.
    """
    string_number = ""
    binary_number = ""

    while decimal_number > 0:
        string_number += str(decimal_number % 2) # Guardar el resto de la div.
        decimal_number //= 2 # Guardar la parte entera de la división.

    for i in range(len(string_number), 0, -1):
        binary_number += string_number[i - 1]

    return int(binary_number)


decimal_num = int(input("Número decimal: "))
binary_num = decimal_to_binary(decimal_num)
print(f"Número binario: {binary_num}")