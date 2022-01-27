
try:
    print(5/0)
except ZeroDivisionError:
    print("No puedes dividir por cero.")


print("\nDame dos números y los dividiré.")
print("Ingresa 's' para salir del programa.")

while True:
    numero_1 = input("\nPrimer número: ")
    if numero_1.lower() == "s":
        break

    numero_2 = input("Segundo número: ")
    if numero_2.lower() == "s":
        break
    
    try:
        respuesta = int(numero_1) / int(numero_2)
    except ZeroDivisionError:
        print("¡No puedes dividir por cero!")
    else:
        print(f"{numero_1} / {numero_2} = {respuesta}")