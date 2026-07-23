import random

greetings = ["Hola", "Salut", "Hello", "Ciao", "Oi", "Yassou", "Hallo"]

random_greet = random.randint(0, len(greetings) - 1)

print(f"{greetings[random_greet]}")