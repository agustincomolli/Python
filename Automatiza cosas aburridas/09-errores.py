def division(dividendo, divisor):
    """Divide un númeropor otro."""
    resultado = dividendo / divisor
    return resultado


try:
    print(f"4 / 2 = {division(4, 2)}")
    print(f"3 / 0 = {division(3, 0)}")
except ZeroDivisionError:
    print("ERROR: Argumento inválido. No se puede dividir por 0.")
