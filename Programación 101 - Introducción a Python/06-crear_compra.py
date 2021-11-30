compras = []

cantidad_items = int(input("¿Cuántos artículos de compra tienes?"))
# cantidad_items = int(cantidad_items)

for numero_item in range(cantidad_items):
    item = input("¿Cuál es el item " + str(numero_item) + "? ")
    compras.append(item)

print(compras)