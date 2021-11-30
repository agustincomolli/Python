# Generar un número aleatorio entre 1 y 5, y permita que el usuario lo adivine.
import random

contar = 0
numero_random = random.randint(1,5)
respuesta = 0

while numero_random != respuesta:
    contar += 1
    numero_random = random.randint(1,5)
    respuesta = input("Adivina un número entre 1 y 5: ")
    
    if respuesta.isnumeric():
        respuesta = int(respuesta)
 

print(f"¡Lo adivinaste en {contar} intentos!")