# Recorriendo una lista.
animals = ["perro", "gato", "loro", "cocodrilo"]
print("Recorrer una lista de animales:")
for animal in animals:
    print(animal)

# Recorrer una lista y hacer varios procesos en cada iteración.
numbers = [10, 6, 1977, 18, 10, 1978]
print("\nRecorrer una lista y procesar datos:")
for number in numbers:
    result = number * 2
    print(result)

# Recorriendo una lista usando la función range()
print("\nRecorrer una lista através de un rango:")
for number in range(10,17):
    print(number)

# Recorrer una lista por su índice. No es óptimo para recorrer conjuntos.
print("\nRecorrer una lista por su índice:")
for index in range(len(animals)):
    print(animals[index])

# Recorrer una lista usando la función enumerate.
print("\nRecorrer una lista usando enumerate():")
for index, animal in enumerate(animals):
    print(f"{index+1} - {animal}")

# Recorrer un diccionario.
user = {
    "nombre" : "Agustín",
    "apellido": "Comolli",
    "edad" : 46,
    "email" : "agustincomolli@gmail.com"
}
print("\nRecorrer un diccionario:")
for key, value in user.items():
    print(f"{key.capitalize()}: {value}")

# Recorrer una lista salteando un elemento o elementos determinados.
print("\nRecorrer una lista salteando un elemento:")
fruits = ["manzana", "banana", "pera", "quinoto", "durazno"]
for fruit in fruits:
    if fruit == "quinoto":
        continue
    print(f"¡Me voy a comer una {fruit}!")

# Recorrer una lista pero detenerse si se cumple una condición.
print("\nRecorrer una lista y detenerse en una condición dada:")
for fruit in fruits:
    print(f"¡Me voy a comer una {fruit}!")
    if fruit == "pera":
        print("Te agarraron ganas de ir al baño, no puedes continuar.")
        break

# Recorriendo una cadena de caracteres o string.
text = "Hola, buenos días"
print("\nRecorriendo una cadena de caracteres:")
for letter in text:
    print(letter)

# Crear una lista usando una sola línea de código: list comprehention.
print("\nCrear una lista usando una sola línea de código:")
table_2 = [number * 2 for number in range(1,11)]
print(f"Tabla del 2: {table_2}")