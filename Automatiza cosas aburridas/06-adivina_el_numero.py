# Este es un juego de adivinanzas.
import random

numero_secreto = random.randint(1, 20)

print("Estoy pensando en un número de 1 a 20.")

# Adivinar el número teniendo hasta 6 oportunidades.
for i in range(1, 7): # El último número no se incluye.
    respuesta = int(input("Haz una conjetura: "))

    if respuesta > numero_secreto:
        print("Tu conjetura es demasiado alta.")
    elif respuesta < numero_secreto:
        print("Tu conjetura es demasiado baja.")
    else:
        break # Encontró el número.

if respuesta == numero_secreto:
    print(f"\n¡Buen trabajo! Adivinaste mi número en {i} intento(s).")
else:
    print("\n¡Nooo! El número en el que estaba pensando era el " + 
        f"{numero_secreto}")