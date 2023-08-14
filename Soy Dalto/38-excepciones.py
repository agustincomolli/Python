def sum():
    # Crear un bucle infinito que sale sólo si la conversión de tipos es
    # válida.
    while True:
        # Intentar converir ingreso a números
        try:
            number_1 = int(input("Número 1: "))
            number_2 = int(input("Número 2: "))
            return number_1 + number_2
        except ValueError:
            # En caso de error, mostrar un mensaje.
            print("\nERROR: No se puede convertir el dato ingresado en un " +
                  "número entero.\n")


result = sum()
print(f"El resultado es {result}")
