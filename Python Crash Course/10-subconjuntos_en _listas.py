jugadores = [
    "Emiliano Martínez", 
    "Nahuel Molina", 
    "Cristian Romero", 
    "Nicolás Otamendi", 
    "Marcos Acuña", 
    "Rodrigo De Paul", 
    "Leandro Paredes", 
    "Giovani Lo Celso", 
    "Ángel Di María", 
    "Lautaro Martínez",
    "Lionel Messi"
    ]

# Imprimir los primeros tres jugadores.
print(jugadores[:3])
# Imprimir solamente los defensores.
print(jugadores[1:5])
# Iterar en un subconjunto de datos.
print("Aquí están los delanteros de la selección:")
for jugador in jugadores[8:]:
    print(jugador)