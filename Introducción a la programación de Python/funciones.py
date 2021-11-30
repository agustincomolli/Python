# Función con dos argumentos para calcular el volumen de un cilindro.
# Esta función tiene un argumento "radio" con un valor predeterminado "5"
def volumen_cilindro(altura, radio=5):
    pi = 3.14159
    volumen = altura * pi * radio ** 2
    return volumen


# Función sin argumentos.
def imprimir_saludo():
    print("¡Hola mundo!")


imprimir_saludo()

print("\nLlamando a la función volumen_cilindro(10, 5)...")
print(volumen_cilindro(10, 5))
print("\nLlamando a la función volumen_cilindro(10)...")
print(volumen_cilindro(10))
print("\nLlamando a la función volumen_cilindro(10, 7)...")
print(volumen_cilindro(10, 7))
