import os
from mylib import color_me, input_color

os.system("clear")
print(color_me("*** Frases multicolor ***\n", "yellow"))
sentence = input_color("¿Qué oración quieres hacer arcoiris?\n> ",
                       color_input="green")

print()
color = ""

for letter in sentence:
    if letter.lower() == "r":
        color = "red"
    elif letter.lower() == "g":
        color = "green"
    elif letter.lower() == "b":
        color = "blue"
    elif letter.lower() == "p":
        color = "magenta"
    elif letter.lower() == "y":
        color = "yellow"
    elif letter == " ":
        color = ""

    print(color_me(letter, color), end="")

print("\n")