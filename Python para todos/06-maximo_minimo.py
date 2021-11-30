ingreso = ""
numero = 0
maximo = -1
minimo = None # Inicializo la variable sin ningún valor.

print("Escriba un número o 'listo' para terminar.\n")
ingreso = input("Número: ")

while ingreso != "listo":
    try:
        numero = int(ingreso)
    except:
        print("ERROR: Escriba un número o 'listo' para terminar.")
        #quit()
    if numero > maximo:
        maximo = numero
    if (minimo is None) or (numero < minimo):
        minimo = numero
    ingreso = input("Número: ")

print("\nEl valor máximo ingresado es:", maximo)
print("El valor mínimo ingresado es:", minimo, "\n")