autos = ["ford", "chevrolet", "renault", "volkswagen", "peugeot"]
# Imprimir lista desordenada.
print("Lista desordenada: " + str(autos).title())
# Ordenar lista de forma permanente.
autos.sort()
print("Lista ordenada [A-Z]: " + str(autos).title())
# Invertir orden.
autos.sort(reverse=True)
print("Lista ordenada [Z-A]: " + str(autos).title())
# Ordenar temporalemente la lista.
autos = ["ford", "chevrolet", "renault", "volkswagen", "peugeot"]
print("\nLista original: " + str(autos).title())
print("Lista ordenada: " + str(sorted(autos)).title())
print("Otra vez la lista original: " + str(autos).title())

# Imprimir una lista en orden inverso sin ordenar.
autos.reverse()
print("Lista en orden inverso: " + str(autos).title())
# Calcular el tamaño de una lista.
tamaño = len(autos)
print("La lista tiene " + str(tamaño) + " items.")