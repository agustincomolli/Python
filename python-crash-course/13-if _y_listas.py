ingredientes_pedidos = []
print("La pizzería de los Hijos de Puta")
print("=" * 33 + "\n")

# Si hay elementos en la lista...
if ingredientes_pedidos:
    for ingrediente in ingredientes_pedidos:
        print("Agregando" + ingrediente + ".")
    print("\n¡Terminamos de preparar tu pizza!")
else:
    print("¿Estás seguro que quieres una pizza sencilla?")

ingredientes_disponibles = ["salame", "tomate", "ajo", "anchoas", "cebolla", 
    "aceitunas", "albahaca"]
ingredientes_pedidos = ["tomate", "ajo", "aceitunas", "aceite de oliva"]

for ingrediente_pedido in ingredientes_pedidos:
    if ingrediente_pedido in ingredientes_disponibles:
        print("Agregando " + ingrediente_pedido + ".")
    else:
        print("Lo siento no tenemos '" + ingrediente_pedido + "'.")

print("\n¡Terminamos de preparar tu pizza!")
