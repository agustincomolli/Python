bicicletas = ["montaña", "paseo", "carreras", "playera"]
# Imprimir toda la lista.
print("Lista de bicicletas:\n\t" + str(bicicletas) + "\n")

# Acceder a items individuales.
print("Primer item: " + bicicletas[0].capitalize())
print("Tercer item: " + bicicletas[2].capitalize())
# Acceder al último item.
print("Último item: " + bicicletas[-1])

# Modificar un item de la lista.
bicicletas[1] = "urbana"
print("\nLista modificada:\n\t" + str(bicicletas).title())

# Agregar un item al final de la lista.
bicicletas.append("cross")
# Insertar un item en un lugar determinado de la lista.
bicicletas.insert(2, "plegable")
print("\nLista agrandada:\n\t" + str(bicicletas).title())

# Eliminar un item determinado de la lista.
del bicicletas[2]
print("\nLista con item eliminado:\n\t" + str(bicicletas).title())
# Eliminar último item y recuperar su valor.
ultimo_item = bicicletas.pop()
# Eliminar el segundo item y recuperar su valor.
segundo_item = bicicletas.pop(1)
print("\nLista acortada:\n\t" + str(bicicletas).title())
print("Último item eliminado: " + ultimo_item.title())
print("Segundo item eliminado: " + segundo_item.title())
# Eliminar items por valor.
bicicletas = ["montaña", "paseo", "carreras", "playera"]
bicicletas.remove("playera")
print("\nLista acortada:\n\t" + str(bicicletas).title())
