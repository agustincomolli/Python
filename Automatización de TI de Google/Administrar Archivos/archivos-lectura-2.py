with open("texto.txt") as archivo:
    # Recorrer todas las líneas del archivo.
    for linea in archivo:
        # Al imprimir las líneas del archivo aparecen líneas en blanco
        # entre cada una, para que no aparezcan usamos el método strip().
        print(linea.strip().upper())

archivo = open("texto.txt")
# Leer todas las líneas y hacer una lista.
lineas = archivo.readlines()
archivo.close()

# Ordenar las líneas de la lista.
lineas.sort()

print("\n Imprimir líneas ordenadas \n")
for linea in lineas:
    print(linea.strip())