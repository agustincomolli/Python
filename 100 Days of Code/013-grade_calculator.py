default_color = "\033[0m"
red_color = "\033[31m"
green_color = "\033[32m"
yellow_color = "\033[33m"
blue_color = "\033[34m"
magenta_color = "\033[35m"
cyan_color = "\033[36m"

print(yellow_color, end="")
print("*** Calculadora de notas de examen ***\n")

exam_name = input("Nombre del examen: " + green_color)
max_punctuation = int(input(yellow_color + "\nLa puntuación máxima es: " + green_color))
punctuation = int(input(yellow_color + "\nTu puntaje: " + green_color))

exam_percentage = (punctuation * 100) / max_punctuation
exam_percentage = round(exam_percentage, 2)

if exam_percentage >= 90:
    grade = "A+ 🏆"
    print(green_color, end="")
elif exam_percentage >= 80:
    grade = "A- 🥳"
    print(cyan_color, end="")
elif exam_percentage >= 70:
    grade = "B 😄"
    print(blue_color, end="")
elif exam_percentage >= 60:
    grade = "C 🙄"
    print(yellow_color, end="")
elif exam_percentage >= 50:
    grade = "D 😢"
    print(magenta_color, end="")
else:
    grade = "U 😭"
    print(red_color, end="")

print(f"\nObtuvo un {exam_percentage}% que es una {grade}" + default_color)