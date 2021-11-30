base = 0
altura = 0

def obtener_area(base, altura):
    return (base * altura) / 2

base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))

print("El área del triángulo es: ", obtener_area(base, altura))