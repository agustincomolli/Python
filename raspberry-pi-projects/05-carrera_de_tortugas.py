from turtle import *
from random import randint

# Dibujar la pista de carreras.
def crear_pista():
    speed(0)
    penup()
    # Ubicar posición inicial.
    goto(-140, 140)
    for pasos in range(15):
        write(pasos, align="center")
        right(90)
        # Dibujar líneas punteadas.
        for i in range(8):
            forward(10)
            pendown()
            forward(10)
            penup()
        backward(160)
        left(90)
        forward(20)


# Crear nueva tortuga.
def crear_tortuga(color, x, y):
    tortuga = Turtle()
    tortuga.color(color)
    tortuga.shape("turtle")
    # Ubicarla
    tortuga.penup()
    tortuga.goto(x, y)
    # Hacer girar en 360°.
    for turno in range(10):
        tortuga.right(36)
    tortuga.pendown()
    return tortuga


crear_pista()
tortuga_roja = crear_tortuga("red", -160, 100)
tortuga_azul = crear_tortuga("blue", -160, 70)
tortuga_verde = crear_tortuga("green", -160, 40)
tortuga_amarilla = crear_tortuga("yellow", -160, 10)

# Hacer correr a las tortugas.
for turno in range(100):
    tortuga_roja.forward(randint(1, 5))
    tortuga_azul.forward(randint(1, 5))
    tortuga_verde.forward(randint(1, 5))
    tortuga_amarilla.forward(randint(1, 5))
# Esperar a que el usuario presion ENTER para salir.
input("Presione ENTER para continuar...")
