# Generar un número aleatorio entre 1 y 10, y permita que el usuario lo adivine.
import random

contar = 0
numero_random = random.randint(1,5)
respuesta = 0

print ("Adivina un número entre 1 y 10:")

while numero_random != respuesta:
    contar += 1
    numero_random = random.randint(1,5)
    
    if respuesta.isnumeric():
        respuesta = int(respuesta)
    else:
        print("Introduzca sólo números, por favor.")
        continue

    if respuesta < 1:
        print("Tu conjetura es demasiado baja, ¡vuelve a intentarlo!")
    elif respuesta > 10:
        print("Tu conjetura es demasiado alta, ¡inténtalo de nuevo!")

print(f"¡Lo adivinaste en {contar} intentos!")