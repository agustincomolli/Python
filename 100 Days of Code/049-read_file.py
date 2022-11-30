from mylib import clear_screen, color_me, input_color

clear_screen()
print(color_me("🌟Lider actual🌟\n", "yellow"))
print("Analizando los puntajes más altos... 🔍")

high_score = 0
name = ""
file = open("./scores.txt", mode="r", encoding="UTF-8")
for line in file.readlines():
    actual_score = line.split()
    if int(actual_score[1]) > high_score:
        high_score = int(actual_score[1])
        name = actual_score[0]

message = f"\nEl líder actual es {name} que tiene "
message += f"{high_score} puntos.\n"
print(color_me(message, "magenta"))
file.close()
