import sqlite3
from random import randint
from time import time

# Abrir la conexión a la base de datos.
conexion = sqlite3.connect("computer_cards.db")

# Leer todos los registros de la tabla computer
def leer_todas_las_cartas():
    registros = conexion.execute("SELECT * FROM computer")
    return registros.fetchall()


# Elegir un registro de forma aleatoria para generar una carta al azar.
def elegir_carta():
    cartas = leer_todas_las_cartas()
    ultima_carta_elegida = leer_ultima_carta_elegida()
    carta_aleatoria = cartas[randint(0, len(cartas) - 1)]

    # Mientras la carta haya sido elegida previamente.
    while carta_aleatoria == ultima_carta_elegida:
        # Volver a seleccionar una carta.
        carta_aleatoria = cartas[randint(0, len(cartas) - 1)]
    
    # Agregar la carta elegida a la tabla picked para seguimiento.
    insertar_carta_elegida(carta_aleatoria[0])
    return carta_aleatoria


# Insertar la carta elegida en la tabla picked.
def insertar_carta_elegida(nombre):
    insert_sql = f"INSERT INTO picked (name, time) VALUES ('{nombre}', {time()})"
    conexion.execute(insert_sql)
    conexion.commit()


# Devolver la última carta elegida.
def leer_ultima_carta_elegida():
    consulta_sql = conexion.execute("SELECT * FROM picked ORDER BY time DESC")
    return consulta_sql.fetchone()


# Dibujar la carta en la pantalla.
def mostrar_carta(carta):
    nombre = str(carta[0])
    nucleos = str(carta[1])
    velocidad = str(carta[2])
    memoria = str(int(carta[3]))
    costo = str(int(carta[4]))
    print("+------------------------------+")
    print("|", " " * 28, "|")
    print("|", nombre.center(28), "|")
    print("|", " " * 28, "|")
    print("|   Núcleos:", " " * 7, nucleos, "        |")
    print("|   Velocidad:", " " * 5, velocidad, "GHz   |")
    
    if len(memoria) == 3:
        print("|   Memoria:", " " * 5, memoria, "  MB    |")
    elif len(memoria) == 4:
        print("|   Memoria:", " " * 4, memoria, "  MB    |")
    else:
        print("|   Memoria:", " " * 3, memoria, "  MB    |")
    
    if len(costo) == 1:
        print("|   Costo:", " " * 9, costo, "  u$s   |")
    elif len(costo) == 2:
        print("|   Costo:", " " * 8, costo, "  u$s   |")
    elif len(costo) == 3:
        print("|   Costo:", " " * 7, costo, "  u$s   |")
    else:
        print("|   Costo:", " " * 6, costo, "  u$s   |")
    print("|", " " * 28, "|")
    print("+------------------------------+")


# Registrar las cartas jugadas y cuál fue la que ganó.
def registrar_juego(carta_ganadora):
    # Recuperar las cartas jugadas en la ronda actual.
    consulta_sql = conexion.execute("SELECT * FROM picked ORDER BY time DESC")
    cartas = consulta_sql.fetchall()
    carta1 = cartas[1]
    carta2 = cartas[0]
    # Agregar las cartas jugadas y la ganadora a la tabla result.
    insert_sql = "INSERT INTO result (card1, card2, winner) "
    insert_sql += f" VALUES ('{carta1[0]}', '{carta2[0]}', '{carta_ganadora[0]}')"
    conexion.execute(insert_sql)
    # Confirmar cambios.
    conexion.commit()
    

jugador = input("¿Es usted el jugador 1 o 2? > ")
jugador_eligiendo = "1"
# Establecer la cantidad de rondas del juego.
rondas = 5
for ronda in range(rondas):
    input("Pulsa INTRO para elegir una carta cuando ambos jugadores estén listos > \n")
    print(f"*** El jugador {jugador_eligiendo} elige ***".center(32))
    carta = elegir_carta()
    mostrar_carta(carta)
    ganador = input("¿Has ganado? (S)í, (N)o, (E)mpate: ").lower()
    if ganador == "s":
        registrar_juego(carta)
        jugador_eligiendo = jugador
    elif ganador == "n":
        if jugador == "1":
            jugador_eligiendo = "2"
        else:
            jugador_eligiendo = "1"

# Cerrar la base de datos.
conexion.close()
