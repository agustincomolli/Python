"""
Valores booleanos equivalentes a True o False.
"""

name = ""

while not name:
    print("Ingrese su nombre")
    name = input("> ")

print("¿Cuántos invitados piensa tener?")
num_of_guests = int(input("> "))

if num_of_guests:
    print("Asegúrese de tener habitaciones suficientes para todos los invitados.")

print("Hecho.")
