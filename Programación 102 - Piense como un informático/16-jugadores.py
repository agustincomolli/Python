jugadores = [
            "Franco Armani",
            "Emiliano Martínez",
            "Agustín Marchesín",
            "Juan Musso",
            "Gonzalo Montiel",
            "Nahuel Molina Lucero",
            "Cristian Romero",
            "Nicolás Otamendi",
            "Lucas Martínez Quarta",
            "Germán Pezzella",
            "Lisandro Martínez",
            "Nicolás Tagliafico",
            "Marcos Acuña",
            "Rodrigo De Paul",
            "Leandro Paredes",
            "Giovani Lo Celso",
            "Exequiel Palacios",
            "Guido Rodríguez",
            "Nicolás Domínguez",
            "Alejandro Gómez",
            "Lionel Messi",
            "Lautaro Martínez",
            "Nicolás González",
            "Sergio Agüero",
            "Ángel Correa",
            "Ángel Di María",
            "Joaquín Correa",
            "Julián Álvarez"
            ]

def seleccionar_jugador(equipo, jugadores):
    from random import choice

    jugador_seleccionado = choice(jugadores)
    equipo.append(jugador_seleccionado)
    jugadores.remove(jugador_seleccionado)


def seleccionar_jugador_mezclando(equipo, jugadores):
    from random import shuffle
    
    shuffle(jugadores)
    equipo.append(jugadores.pop())

def crear_equipo(jugadores, cantidad):
    from random import sample

    equipo = sample(jugadores, cantidad)
    return equipo


equipo_local = []
equipo_visitante = []

for i in range(11):
    seleccionar_jugador_mezclando(equipo_local, jugadores)
    # seleccionar_jugador(equipo_visitante,jugadores)

equipo_visitante = crear_equipo(jugadores, 11)

print("\nEquipo local:\n", equipo_local, "\n\nEquipo visitante:\n", equipo_visitante)