guess = 0
tries = 0

print("Adivina el número 🔢:\n")
while guess != 6 and tries < 3:
    guess = int(input("Adivina el número: "))
    tries += 1

if guess == 6:
    print("¡Lo tienes!")
else:
    print("Mejor suerte para la próxima.")