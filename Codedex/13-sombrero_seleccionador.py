"""
Escriba un programa sortinghat.py que le haga al usuario algunas preguntas
usando int()y lo coloque en una de las casas según sus respuestas.

"""

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print(f"Sombrero seleccionador 🎩\n{'*'*26}")

question_1 = """
A - ¿Te gusta el Amanecer o el Anochecer?
    1) Amanecer
    2) Anochecer
"""
question_2 = """
B - Cuando esté muerto, quiero que la gente me recuerde como:
    1) El Bueno
    2) El Grande
    3) El Sabio
    4) El Audaz
"""
question_3 = """
C - ¿Qué tipo de instrumento agrada más a tu oído?
    1) El violín
    2) La trompeta
    3) El piano
    4) El tambor
"""

print(question_1)
answer = int(input("Elige una opción: "))

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Entrada incorrecta")

print(question_2)
answer = int(input("Elige una opción: "))

if answer == 1:
    hufflepuff += 1
elif answer == 2:
    slytherin += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:
    gryffindor += 1
else:
    print("Entrada incorrecta")

print(question_3)
answer = int(input("Elige una opción: "))

if answer == 1:
    slytherin += 1
elif answer == 2:
    hufflepuff += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:
    gryffindor += 1
else:
    print("Entrada incorrecta")


print("\n🎩 ¡El sombrero mágico ha elegido!")


if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print("\n Eres de: 🦁 ¡Ggryffindor!")
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print("\n Eres de: 🦅 ¡Ravenclaw!")
elif hufflepuff >= slytherin:
    print("\n Eres de: 🦡 ¡Hufflepuff!")
else:
    print("\n Eres de: 🐍 ¡Slytherin!")

