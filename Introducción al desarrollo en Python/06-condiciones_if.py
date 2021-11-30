try:
    precio = float(input("¿Cuánto tiene que pagar? $ "))
except:
    print("ERROR. Debe ingresar un número!")
    quit()

if precio >= 1:
    impuesto = 0.07
else:
    impuesto = 0

print(f"La tasa de impuesto es de {impuesto}")

# Al comparar cadenas es importante recordar que Python es case sensitive.
pais = input("\nIngrese el nombre de su país: ")
if pais.lower() == "argentina":
    print("¡Seguro que te gusta el asado!")
else:
    print("No sos de Argentina.\n")