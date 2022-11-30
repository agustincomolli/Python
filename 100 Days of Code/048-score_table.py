from mylib import clear_screen, color_me, input_color
import time

clear_screen()

print(color_me("🌟 TABLA DE PUNTUACION 🌟\n", "yellow"))

file = open("./scores.txt", encoding="UTF-8", mode="a+")

while True:
    initials = input_color("Ingrese sus iniciales: ", color_input="green")
    score = input_color("Ingrese su puntuación: ", color_input="green")
    if not score.isnumeric():
        print(color_me("ERROR: Debe ingresar un número", "red"))
        time.sleep(3)
        continue

    file.write(f"{initials.upper()} {score}\n")
    
    another = input_color("¿Agregar otro? [s|n]: ", color_input="green")
    if another.strip().lower()[0] != "s":
        break

file.close()
