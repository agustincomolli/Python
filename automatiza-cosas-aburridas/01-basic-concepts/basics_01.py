"""
Este programa dice Hola y solicita mi nombre.
"""

print("¡Hola mundo!")

print("¿Cuál es tu nombre? ") # Pedir el nombre
my_name = input("> ")
print("Es bueno conocerte, " + my_name)
print("El largo de tu nombre es: ")
print(len(my_name))

print("¿Qué edad tienes?") # Pedir la edad
my_age = input("> ")
print("Tendrás", str(int(my_age) + 1), "años el año que viene.")
