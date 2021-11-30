from random import choice

jugadores = []
equipo_a = []
equipo_b = []
equipos = []
nombre_a = ""
nombre_b = ""

# Seleccionar un jugador al azar.
def seleccionar_jugador():
    jugador = choice(jugadores)
    jugadores.remove(jugador)
    return jugador


# Seleccionar un equipo al azar.
def seleccionar_equipo():
    equipo = choice(equipos)
    equipos.remove(equipo)
    return equipo
# Leer la lista de jugadores desde un archivo.
with open("06-lista_jugadores.txt", mode="r", encoding="UTF-8") as archivo:
    jugadores = archivo.read().splitlines()

# Leer la lista de equipos en un archivo.
with open("06-lista_equipos.txt", mode="r", encoding="UTF-8") as archivo:
    equipos = archivo.read().splitlines()

# Crear los equipos de jugadores.
while len(jugadores) > 0:
    equipo_a.append(seleccionar_jugador())
    if len(jugadores) == 0:
        jugadores.append(equipo_a.pop())
        break
    equipo_b.append(seleccionar_jugador())

# Seleccionar equipos.
nombre_a = seleccionar_equipo()
nombre_b = seleccionar_equipo()
print("Seleccionador de equipos:\n" + "=" * 25)
print(f"\nEquipo {nombre_a}: {equipo_a}")
print(f"Equipo {nombre_b}: {equipo_b}")
print(f"Sin jugar: {jugadores}\n")