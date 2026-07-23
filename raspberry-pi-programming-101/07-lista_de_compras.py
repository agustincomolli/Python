print("*** Bienvenido al programa de lista de compras ***\n")
compras = []

cantidad_items = input("¿Cuántos artículos de compra tiene? ")
cantidad_items = int(cantidad_items)

for numero_item in range(cantidad_items):
    item = input("¿Cuál es el item " + str(numero_item) + "? ")
    compras.append(item)

print("\n Aquí está su lista de compras:")
contador = 0
for item in compras:
    contador += 1
    print(contador, " - ", item)

print(f"\nTiene {len(compras)} artículos en su lista de compras\n")