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

# Copiar una lista.
comidas = ["pizza", "fideos", "polenta", "arroz"]
mis_comidas = comidas[:]
comidas.append("ensaladas")
mis_comidas.append("tortilla")

print("\nLista de comidas: " + str(comidas))
print("Lista de mis comidas: ")
for mi_comida in mis_comidas:
    print("    " + mi_comida.capitalize())
