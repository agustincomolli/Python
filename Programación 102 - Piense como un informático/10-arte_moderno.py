from turtle import *
from random import *

# Generar un color RGB aleatorio
def color_aleatorio():
    colormode(255)

    rojo = randint(0, 255)
    verde = randint(0, 255)
    azul = randint(0, 255)
    return (rojo, verde, azul)

# Mover tortuga a una posición aleatoria
def posicion_aleatoria(tortuga):
    # Generar las coordenadas aleatorias.
    x = randint(-100, 100)
    y = randint(-100, 100)
    # Subir el lápiz para no escribir mientras se mueve.
    tortuga.penup()
    # Ir a la posición generada.
    tortuga.goto(x, y)
    # Bajar el lápiz para empezar a escribir.
    tortuga.pendown()

def rumbo_aleatorio():
    return randint(1, 360)

def dibujar_rectangulo():
    tortuga = Turtle()
    # Establecer la forma de la tortuga.
    tortuga.shape("turtle")
    # Esconder tortuga.
    tortuga.hideturtle()
    # Establecer la velocidad de dibujo.
    tortuga.speed(0)
    posicion_aleatoria(tortuga)
    tortuga.color(color_aleatorio())
    
    ancho = randint(10, 100)
    alto = randint(10, 100)
    
    # Dibujar el rectángulo.
    tortuga.begin_fill()
    for i in range(2):
        tortuga.forward(ancho)
        tortuga.right(90)
        tortuga.forward(alto)
        tortuga.right(90)
    tortuga.end_fill()

def dibujar_circulo():
    tortuga = Turtle()
    tortuga.hideturtle()
    tortuga.speed(0)
    tortuga.color(color_aleatorio())
    posicion_aleatoria(tortuga)

    tortuga.dot(randint(10, 200))

def dibujar_estrella():
    tamaño = randint(20, 100)
    tortuga = Turtle()
    tortuga.hideturtle()
    tortuga.speed(0)
    tortuga.color(color_aleatorio())
    posicion_aleatoria(tortuga)
    tortuga.setheading(rumbo_aleatorio())

    tortuga.begin_fill()
    for lado in range(5):
        tortuga.left(144)
        tortuga.forward(tamaño)
    tortuga.end_fill()

# verdurita = Turtle()
# verdurita.shape("turtle")

# for i in range(30):
#     verdurita.color(color_aleatorio())
#     verdurita.setheading(rumbo_aleatorio())
#     posicion_aleatoria(verdurita)
#     verdurita.stamp()

# verdurita.hideturtle()
# verdurita.clear()

# Dibujar 20 rectángulos aleatorios.
for i in range(20):
    # dibujar_rectangulo()
    # dibujar_circulo()
    dibujar_estrella()

input("Presione una tecla para continuar...")