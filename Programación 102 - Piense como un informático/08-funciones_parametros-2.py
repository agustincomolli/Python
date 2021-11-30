from turtle import Turtle

verdurita = Turtle()

# Devuelve el área de un círculo.
def area_circulo(radio):
    return 3.14 * radio * radio

# Devuelve la circunferencia de un círculo.
def circunferencia(radio):
    import math
    return math.pi * 2 * radio

def dibujar_circulo(tortuga, radio, color):
    tortuga.color(color)
    tortuga.dot(radio * 2)

    tortuga.color("black")
    # Mueve la tortuga para que los mensajes no se superpongan.
    tortuga.goto(0, 6)
    tortuga.write(f"Area: {str(area_circulo(radio),)}", align = "center")
    tortuga.goto(0, -6)
    tortuga.write(f"Circunferencia: {str(circunferencia(radio),)}", align = "center")
    tortuga.hideturtle()

dibujar_circulo(verdurita, 150, "light blue")
dibujar_circulo(verdurita, 100, "white")
dibujar_circulo(verdurita, 50, "yellow")
input("Presione ENTER para terminar...")