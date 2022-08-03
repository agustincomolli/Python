# Convertir números decimales en binarios.

def decimal_to_binary(decimal_number:int) -> int:
    """
        DESCRIPTION: Convierte un número decimal en binario.
        PARAMETERS: decimal_number = número entero decimal.
    """
    string_number = ""
    binary_number = ""

    while decimal_number > 0:
        # Guardar el resto de la div.
        string_number = str(decimal_number % 2) + string_number 
        # Guardar la parte entera de la división.
        decimal_number //= 2 

    return int(string_number)


decimal_num = int(input("Número decimal: "))
binary_num = decimal_to_binary(decimal_num)
print(f"Número binario: {binary_num}")