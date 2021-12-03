# Imprimir una lista de números.
for i in range(1, 5):
    print(i)

# Crear una lista de números.
numeros = list(range(1, 5))
print("Lista de números: " + str(numeros))

numeros_pares = list(range(2, 11, 2))
print("Número pares: " + str(numeros_pares))

# Crear lista de cuadrados.
cuadrados = []

for valor in range(1, 11):
    # cuadrado = valor ** 2
    # cuadrados.append(cuadrado)
    cuadrados.append(valor ** 2)

# List Comprehensions.
cuadrados = [valor **2 for valor in range(1, 11)]

print("Lista de cuadrados: " + str(cuadrados))