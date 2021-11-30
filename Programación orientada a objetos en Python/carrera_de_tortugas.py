from turtle import Turtle
from random import randint

agustin = Turtle()
agustin.color("green")
agustin.shape("turtle")

agustin.penup()
agustin.goto(-160, 100)
agustin.pendown()

lorena = Turtle()
carlitos = Turtle()
adrian = Turtle()

lorena.color("pink")
lorena.shape("turtle")
lorena.penup()
lorena.goto(-160, 70)
lorena.pendown()

carlitos.color("blue")
carlitos.shape("turtle")
carlitos.penup()
carlitos.goto(-160, 40)
carlitos.pendown()

adrian.color("red")
adrian.shape("turtle")
adrian.penup()
adrian.goto(-160, 10)
adrian.pendown()

for movimiento in range(100):
    agustin.forward(randint(1, 5))
    lorena.forward(randint(1, 5))
    carlitos.forward(randint(1, 5))
    adrian.forward(randint(1, 5))

input("Presione Entrar para salir...")