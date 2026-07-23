import random

green_color = "\033[32m"
default_color = "\033[0m"
secret_number = random.randint(1, 1000000)
attempts = 0
number = 0

print("*** Adivina el número 🤔 ***")

while True:
    attempts += 1

    print("\nDe 0 a 1.000.000, ¿cuál es el número?")
    number = int(input("\nNúmero 👉 " + green_color))
    print(default_color, end="")

    if number == secret_number:
        print("\n¡Correcto, has adivinado!¡Felicitaciones .🥳!")
        print(f"Lo has logrado en {attempts} intentos.")
        break
    elif number > secret_number and number < 1000000:
        print("\nEl número es muy alto.")
    elif number < secret_number and number >0:
        print("\nEl número es muy bajo.")
    elif number < 0:
        print("\nSaliendo...")
        exit()
    else:
        print("\nERROR: Intentelo de nuevo.")