from turtle import Turtle

# Calcula la superficie de un rectángulo.
def calcular_superficie(alto, ancho):
    return (alto * 2) + (ancho * 2)

# Calcula el área de un rectángulo.
def calcular_area(alto, ancho):
    return alto * ancho

# Escribe texto en una ubicación dada.
def escribir_texto(coordenadas, texto):
    tortuga = Turtle()
    # Ocultar tortuga.
    tortuga.hideturtle()
    tortuga.color("black")
    # Alzar lápiz.
    tortuga.penup()
    tortuga.goto(coordenadas)
    tortuga.pendown()
    tortuga.write(texto, align="center")
    tortuga.penup()


def dibujar_rectangulo(alto, ancho, color):
    tortuga = Turtle()
    # Establecer la forma de la tortuga.
    tortuga.shape("turtle")
    # Esconder tortuga.
    tortuga.hideturtle()
    # Establecer la velocidad de dibujo.
    tortuga.speed(0)
    tortuga.color(color)
  
    # Dibujar el rectángulo.
    tortuga.begin_fill()
    for i in range(2):
        tortuga.forward(ancho)
        tortuga.right(90)
        tortuga.forward(alto)
        tortuga.right(90)
    tortuga.end_fill()

    coordenadas = (ancho / 2, -(alto / 2))
    mensaje = f"Superficie: {str(calcular_superficie(alto, ancho))}"
    escribir_texto(coordenadas, mensaje)

    coordenadas = (ancho / 2, -(alto / 2) - 15)
    mensaje = f"Area: {str(calcular_area(alto, ancho))}"
    escribir_texto(coordenadas, mensaje)


dibujar_rectangulo(50, 300, "light green")

input("Presione ENTER para terminar...")