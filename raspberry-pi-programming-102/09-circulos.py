from turtle import Turtle, begin_fill

def dibujar_circulos(x, y, color, tamaño):
    tortuga = Turtle()
    tortuga.color(color)
    tortuga.penup()
    tortuga.goto(x, y)
    tortuga.pendown()
    tortuga.dot(tamaño)

dibujar_circulos(50, 120, "dark green", 30)
dibujar_circulos(-100, 40, "red", 100)

input("Presione una tecla para continuar...")