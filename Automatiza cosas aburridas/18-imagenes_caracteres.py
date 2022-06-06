tabla = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.','.', '.']
        ]
nueva_tabla = []

# len(tabla)-1 me da el número de filas = 8
# len(tabla[0])-1 me da el número de columnas = 5

def crear_fila(tabla, indice_x):
    """Crear una nueva fila con los elementos de la columna indice_x."""
    nueva_fila = []
    for indice_y in range(len(tabla)-1, -1, -1):
        nueva_fila.append(tabla[indice_y][indice_x])
    return nueva_fila

for indice_x in range(len(tabla[0])):
    nueva_tabla.append(crear_fila(tabla, indice_x))

for fila in nueva_tabla:
    for item in fila:
        print(item, end="")
    print("")