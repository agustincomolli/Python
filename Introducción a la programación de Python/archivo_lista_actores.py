def crear_lista_actores(nombre_archivo):
    lista_actores = []
    # use with to open the file nombre_archivo
    # use the for loop syntax to process each line
    # and add the actor name to lista_actores

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            # crear una lista dividiendo la linea hasta la
            # primer "," y tomar el primer elemento que sería
            # el nombre del actor.
            actor = linea.split(",")[0]
            lista_actores.append(actor)

    return lista_actores


lista_actores = crear_lista_actores('actores.txt')
for actor in lista_actores:
    print(actor)
