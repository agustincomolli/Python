# Calcular el área de un triángulo.
altura = 0
base = 0
area = 0

def calcular_area():
    area = (base * altura) / 2
    print(f"El área del triángulo es {area}")

# Pedir al usuario la altura y la base del triángulo.
base = int(input("Ingrese la base del triángulo: "))
altura = int(input("ingrese la altura del triángulo: "))

calcular_area()