"""
Ingresar una línea llena de números y sumarlos fácilmente.

"""

number = input("Ingrese una línea de números separados por un espacio: ")

if number == "":
    print("No has ingresado nada.")
    exit()

number_list = number.split()
sum = 0

try:
    for number in number_list:
        sum += float(number)
    print(f"El total es: {sum}")
except:
    print(sum, "no es un número.")
