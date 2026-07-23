from turtle import *

colores = {
        "muy_lima" : "#A7E30E",
        "real_frambuesa" : "#FA057F",
        "naranja_asombroso" : "#ff8400"
        }

# Definir tamaño y color de la ventana.
def preparar_pantalla():
    pantalla = Screen()
    pantalla.setup(400, 400)
    pantalla.bgcolor(colores["muy_lima"])
    dot(300)


# Escribir un saludo.
def escribir_saludo():
    penup()
    color(colores["real_frambuesa"])
    estilo = ("Lucida Handwriting", 40, "bold")
    write("¡HOLA", font=estilo, align="center")
    right(90)
    forward(60)
    color(colores["naranja_asombroso"])
    write("Mundo!", font=estilo, align="center")
    forward(115)
    left(90)
    forward(170)
    color("white")
    write("- Agustín Comolli", font=("Arial", 12, "bold"), align="right")
    hideturtle()


preparar_pantalla()
escribir_saludo()
input()
