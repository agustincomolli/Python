from clase_randomwalk import RandomWalk

import matplotlib.pyplot as plotter

# Sigue realizando nuevos paseos, mientras el programa esté activo.
while True:
    # Hacer un camino aleatorio e imprimir los puntos.
    camino = RandomWalk(50000)
    camino.llenar_camino()

    # Establecer el tamaño de la ventana.
    plotter.figure(figsize=(10, 6))

    numero_puntos = list(range(camino.num_puntos))

    plotter.scatter(camino.valores_x, camino.valores_y, c=numero_puntos, 
        cmap=plotter.cm.Blues, edgecolors="none", s=1)

    # Enfatizar los primeros y los últimos puntos.
    plotter.scatter(0, 0, c="green", edgecolors="none", s=100)
    plotter.scatter(camino.valores_x[-1], camino.valores_y[-1], c="red", 
        edgecolors="none", s=100)

    # Remover ejes.
    ax = plotter.gca() # Obtener ejes actuales (Get Current Axes)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plotter.show()

    seguir = input("¿Hacer otro camino? (s/n): ")
    if seguir == "n":
        break