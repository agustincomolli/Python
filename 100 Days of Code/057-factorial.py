from mylib import clear_screen, color_me, input_color


def factorial(number: int):
    if number == 1:
        return 1

    return number * factorial(number - 1)


clear_screen()
print(color_me("🌟 Recursividad 🌟\n", "yellow"))
number = input_color("Ingrese un número: ", color_input="green")
if not number.isnumeric():
    print(color_me("\nERROR: El valor ingresado no es un número."))
else:
    print(color_me(f"\nCalculando el factorial de {number}... ",
                   "blue"), end="")
    print(factorial(int(number)))
