# Juego de la vida de Conway.
import random, time

ancho = 60
alto = 20

# Crear una matriz de celdas.
celdas = []
for x in range(ancho):
    columna = [] # Crear una nueva columna.
    for y in range(alto):
        if random.randint(0,1) ==0:
            columna.append("#") # Agregar una celda viva.
        else:
            columna.append(" ") # Agregar una celda muerta.
    celdas.append(columna) # Agregar la columna a las celdas.

while True: # Bucle principal.
    print("\n\n\n\n\n") # Separar cada paso con líneas nuevas.
    celdas_actuales = celdas[:] 

    # Imprimir las celdas en la pantalla.
    for y in range(alto):
        for x in range(ancho):
            print(celdas_actuales[x][y], end="")
        print() # Imprimir una nueva línea al final de la fila.

    # Calcular las celdas del siguiente paso en función de las celdas del 
    # paso actual.
    for x in range(ancho):
        for y in range(alto):
            # Obtener coordenadas vecinas.
            # "% ANCHO" asegura que la coordenada izquierda esté siempre 
            # entre 0 y ANCHO - 1.
            izquierda = (x - 1) % ancho
            derecha = (x + 1) % ancho
            arriba = (y - 1) % alto
            abajo = (y + 1) % alto

            # Contar el número de vecinos vivos.
            vecinos_vivos = 0
            if celdas_actuales[izquierda][arriba] == "#":
                vecinos_vivos += 1 # El vecino superior izquierdo está vivo.
            elif celdas_actuales[x][arriba] == "#":
                vecinos_vivos += 1 # El vecino superior está vivo.
            elif celdas_actuales[derecha][arriba] == "#":
                vecinos_vivos += 1 # El vecino superior derecho está vivo.
            elif celdas_actuales[izquierda][y] == "#":
                vecinos_vivos += 1 # El vecino izquierdo está vivo.
            elif celdas_actuales[derecha][y] == "#":
                vecinos_vivos += 1 # El vecino derecho está vivo.
            elif celdas_actuales[izquierda][abajo] == "#":
                vecinos_vivos += 1 # El vecino inferior izquierdo está vivo.
            elif celdas_actuales[x][abajo] == "#":
                vecinos_vivos += 1 # El vecino inferior está vivo.
            elif celdas_actuales[derecha][abajo] == "#":
                vecinos_vivos += 1 # El vecino inferior derecho está vivo.

            # Establecer la celda según las reglas del Juego de la vida de 
            # Conway:
            if celdas_actuales[x][y] == "#" and (vecinos_vivos == 2 or 
            vecinos_vivos ==3):
                # Las celdas vivas con 2 o 3 vecinas permanecen vivas.
                celdas[x][y] = "#"
            elif celdas_actuales[x][y] == " ":
                # Las celdas muertas con 3 vecinas cobran vida.
                celdas[x][y] = "#"
            else:
                # Todo lo demás muere o permanece muerto.
                celdas[x][y] = " "

    time.sleep(1) # Agregue una pausa de 1 segundo para reducir el parpadeo.