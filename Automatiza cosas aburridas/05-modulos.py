import time
import random
import sys

print("Cuenta regresiva:")
for i in range(5, -1, -1):
    print(i)
    time.sleep(1)
print("¡Boom!")

print("\nDame unos números aleatorios:")
for i in range(5):
    print(random.randint(1, 10))

print("\nSalir del programa sin terminar terminar de ejecutar todo su código:")
while True:
    respuesta = input("Escriba 'salir' para terminar: ")
    if respuesta == "salir":
        sys.exit()
    print(f"Usted escribió '{respuesta}'")