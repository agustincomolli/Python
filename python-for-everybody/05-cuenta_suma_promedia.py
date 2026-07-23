ingreso = ""
numero = 0
cuenta = 0
suma = 0
print("Escriba un número o 'listo' para terminar.\n")
ingreso = input("Número: ")
while ingreso != "listo":
    try:
        numero = int(ingreso)
    except:
        print("ERROR: Escriba un número o 'listo' para terminar.")
        quit()
    cuenta += 1
    suma += numero
    ingreso = input("Número: ")
print("\nSe han ingresado", cuenta, "números.")
print("La suma total es:", suma)
print("El promedio es:", suma / cuenta,"\n")