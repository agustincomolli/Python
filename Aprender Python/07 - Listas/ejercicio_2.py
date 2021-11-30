# Comprobar la inclusión de un valor en una lista.
print("\nPaso 1: \n********")

numeros = [1, 3, 5]

print(5 in numeros)
print(8 in numeros)

print(5 not in numeros)
print(8 not in numeros)

# Recorrer en bucle por una lista.
print("\nPaso 2: \n********")

pueblos = ["Máximo Paz", "Vicente Casares", "Uribelarrea", "Udaondo"]

for pueblo in pueblos:
    print(pueblo)

# Interrumpir un bucle for.
print("\nPaso 3: \n********")

numeros = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numeros.sort()

for numero in numeros:
    if numero > 42:
        break
    print(numero)

# Usar la instrucción else.
print("\nPaso 4: \n********")

import random

numeros = []

while len(numeros) < 5:
    numeros.append(random.randint(1, 100))

for numero in numeros:
    print(numero)
    if numero >= 90:
        print("Encontrado al menos un número mayor que 90")
        break
else:
    print("No hay números mayores de 90")

print("Completado")

# Usar la instrucción continue.
print("\nPaso 5: \n********")

valores = ["notebook", 7, "celular", 3, "camara", 5]
equipamiento = []

for valor in valores:
    if isinstance(valor, str) == False:
        continue
    equipamiento.append(valor)

print(equipamiento)

# Crear bucles anidados.
print("\nPaso 6: \n********")

palos_de_cartas = ["Corazones", "Diamantes", "Tréboles", "Picas"]
numeros_de_cartas = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "As"]

for palo in palos_de_cartas:
    for numero in numeros_de_cartas:
        print(f"{numero} de {palo}")

# Selección aleatoria en una lista.
print("\nPaso 7: \n********")

import random

numeros = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numero_seleccionado = random.choice(numeros) # Seleccionar un elemento al azar.
print(numero_seleccionado)

numeros_seleccionados = random.choices(numeros, k=3) # Seleccionar varios elementos al azar
print(numeros_seleccionados)
