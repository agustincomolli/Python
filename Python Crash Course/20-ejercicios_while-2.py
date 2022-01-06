# Deli: Haga una lista llamada sandwich_orders y llénela con los nombres 
# de varios sándwiches. Luego haz una lista vacía llamada sandwiches 
# terminados. Recorra la lista de pedidos de sándwiches e imprima un 
# mensaje para cada pedido, como "Hice su sándwich de atún". A medida que 
# se hace cada sándwich, muévalo a la lista de sándwiches terminados. 
# Después de que se hayan preparado todos los sándwiches, imprima un mensaje 
# que enumere cada sándwiches que se prepararon.

# Sin jamón y queso: Usando la lista sandwich_orders del Ejercicio anterior, 
# asegúrese de que el sandwich 'jamón y queso' aparezca en la lista al menos tres 
# veces. Agregue código cerca del comienzo de su programa para imprimir un 
# mensaje que diga que el deli se ha quedado sin jamón y queso, y luego use un 
# ciclo while para eliminar todas las apariciones de 'pastrami' de 
# sandwich_orders. Asegúrese de que no terminen los sándwiches de jamón y queso 
# en sandwiches terminados.

sanguches_pedidos = ["jamón y queso", "milanesa", 
    "jamón y queso", "hamburguesa", "milanesa", "jamón y queso"]
sanguches_terminados = []

print("\n¡Nos quedamos sin jamón!\n")
while sanguches_pedidos:
    sanguche = sanguches_pedidos.pop()
    if sanguche == "jamón y queso":
        continue
    print(f"Sanguche de {sanguche} terminado")    
    sanguches_terminados.append(sanguche)

print("\nSe han preparado los siguientes sanguches:")

for sanguche in sanguches_terminados:
    print(f"- {sanguche}")