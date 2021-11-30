from turtle import Turtle

# Dibuja un pentágono
def dibujar_pentagono(color):
    tortuga = Turtle()
    tortuga.hideturtle()
    tortuga.color(color)

    tortuga.begin_fill()
    for i in range(5):
        tortuga.forward(100)
        tortuga.left(72)
    tortuga.end_fill()


dibujar_pentagono("gold")
input("Presione ENTER para terminar...")