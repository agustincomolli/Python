defaul_color = "\033[0m"
yellow_color = "\033[33m"
green_color = "\033[32m"
blue_color = "\033[34m"
red_color = "\033[31m"

print(yellow_color + "*** Juego de Matemáticas ***\n" + defaul_color)

multiplication = int(input("Tabla de multiplicar: " + green_color))
score = 0

for i in range(1, 11):
    print(defaul_color)
    print(f"{multiplication} x {i} =")
    
    result = int(input(green_color))

    if result == i * multiplication:
        print(blue_color + "¡Buen trabajo! 🥳")
        score += 1
    else:
        print(red_color + f"¡Noo! 😭 La respuesta es {i * multiplication}")

print(defaul_color)
print(f"Tu puntaje es {score} de 10")