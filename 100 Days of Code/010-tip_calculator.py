green_color = "\033[32m"
default_color = "\033[0m"
yellow_color = "\033[33m"

print(yellow_color, end="")
print("*** Calculador de Propinas ***")
print()

bill = float(input("¿Cuánto gastaste?\n" + green_color + "$ "))

tip = int(input(yellow_color + "¿Qué porcentaje quieres dar de propina?\n" + green_color))

people = int(input(yellow_color + "¿Cuántas personas son?\n" + green_color))

bill += bill * (tip / 100)

final_amount = round(bill / people, 2)

print(yellow_color + "\nCada uno debe pagar $", final_amount)