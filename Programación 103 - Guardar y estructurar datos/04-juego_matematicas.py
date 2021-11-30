import matplotlib.pyplot as plot

puntuaciones = []
nombres = []

# Cargar las puntuaciones más altas del juego, que están
# almacenadas en un archivo de texto.


def cargar_puntuaciones():
    print("Cargando puntuaciones más altas...")
    try:
        with open("puntuacion_mas_alta.txt", mode="r") as archivo:
            for linea in archivo:
                linea = linea.strip("\n")
                linea = linea.split(" ")
                nombres.append(linea[0])
                puntuaciones.append(int(linea[1]))
    except FileNotFoundError:
        print("No existe el archivo de puntuaciones.")

# Mostrar las puntuaciones más altas.


def mostrar_puntuaciones():
    print("\nPuntuaciones más altas:")
    for posicion in range(len(nombres)):
        print(f"{posicion + 1} - {nombres[posicion]} {puntuaciones[posicion]}")

    plot.bar(nombres, puntuaciones)
    plot.title("Puntajes altos del juego de matemáticas")
    plot.ylabel("Puntajes")
    plot.xlabel("Jugadores")
    plot.show()

# Comparar la puntuación del jugador con el ranking de puntuaciones.


def comparar_puntuacion(puntuacion_jugador, nombre_jugador, nombres,
                        puntuaciones):
    posicion = 0
    for puntuacion in puntuaciones:
        if puntuacion_jugador < puntuacion:
            posicion += 1
    puntuaciones.insert(posicion, puntuacion_jugador)
    nombres.insert(posicion, nombre_jugador)
    puntuaciones = puntuaciones[:10]
    nombres = nombres[:10]

# Guardar las puntuaciones en un archivo de texto.


def guardar_puntuaciones():
    print("Guardando las puntuaciones en un archivo...")
    with open("puntuacion_mas_alta.txt", mode="w") as archivo:
        for posicion in range(len(nombres)):
            archivo.write(f"{nombres[posicion]} {puntuaciones[posicion]}\n")

# Mostrar al usuario la pregunta.


def pregunta_1():
    print("\nPregunta 1: ¿Cuál es el producto de 2x2x2?")

    respuesta = int(input("Tu respuesta:>> "))

    if respuesta == 8:
        return True
    else:
        return False


def pregunta_2():
    print("\nPregunta 2: ¿Cuál es el resultado de 2 - 2 + 2?")

    respuesta = int(input("Tu respuesta:>> "))

    if respuesta == 2:
        return True
    else:
        return False


def pregunta_3():
    print("\nPregunta 3: ¿Cuál es el producto de 8 % 2 x 2?")

    respuesta = int(input("Tu respuesta:>> "))

    if respuesta == 8:
        return True
    else:
        return False


cargar_puntuaciones()
mostrar_puntuaciones()

while True:
    puntuacion = 0

    print("Bienvenido al cuestionario de matemáticas")
    print("¿Puede responder tres preguntas y obtener la máxima puntuación?")

    jugador = input("Ingresa tu nombre: ")

    if pregunta_1():
        print("Correcto")
        puntuacion = puntuacion + 1
        print("Tu puntaje es", puntuacion)
    else:
        print("Incorrecto, la respuesta es 8")
        print("Tu puntaje es", puntuacion)

    if pregunta_2():
        print("Correcto")
        puntuacion = puntuacion + 1
        print("Tu puntaje es", puntuacion)
    else:
        print("Incorrecto, la respuesta es 2")
        print("Tu puntaje es", puntuacion)

    if pregunta_3():
        print("Correcto")
        puntuacion = puntuacion + 1
        print("Tu puntaje es", puntuacion)
    else:
        print("Incorrecto, la respuesta es 8")
        print("Tu puntaje es", puntuacion)

    comparar_puntuacion(puntuacion, jugador, nombres, puntuaciones)
    mostrar_puntuaciones()
    guardar_puntuaciones()
