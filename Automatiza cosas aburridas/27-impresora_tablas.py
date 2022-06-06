def imprimir_tabla(tabla):
    """Imprimir la tabla con formato ajuste derecho."""

    datos_formateados = ""
    # Obtener ancho máximo de cada columna.
    ancho_cols = [0] * len(tabla) # Obtiene cant de columnas de la tabla.
    for columna in range(len(tabla)):
        col_ancha = len(tabla[columna][0])
        for fila in range(len(tabla[columna])):
            if len(tabla[columna][fila]) > col_ancha:
                col_ancha = len(tabla[columna][fila])
        ancho_cols[columna] = col_ancha

    for fila in range(len(tabla[0])):
        for columna in range(len(tabla)):
           datos_formateados += str(tabla[columna][fila]). \
               rjust(ancho_cols[columna]) + " "
        datos_formateados += "\n"
    
    print(datos_formateados)


tabla_de_datos = [['manzanas', 'naranjas', 'cerezas', 'plátano'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['perros', 'gatos', 'alces', 'ganso']]
print(f"Impresora de tablas:\n{'*' * 20}")
imprimir_tabla(tabla_de_datos)
