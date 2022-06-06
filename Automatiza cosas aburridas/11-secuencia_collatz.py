def collatz(numero):
    """Secuencia de Collatz."""
    if numero % 2 == 0:
        return int(numero // 2)
    else:
        return int(numero * 3 + 1)


print("--- SECUENCIA DE COLLATZ ---")
try:
    numero = int(input("\nIngrese un número: "))
except ValueError:
    print("ERROR: El valor ingresado no es un número.")
    exit()
print()

while numero != 1:
    numero = collatz(numero)
    print(numero)

print()