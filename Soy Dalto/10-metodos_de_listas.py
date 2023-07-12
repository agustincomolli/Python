# Contar los elementos de una lista.
my_data = ["Agustín", "Rivadavia", 340, 46, "agustincomolli@gmail.com"]
print(f"La lista tiene {len(my_data)} elementos.")

# Agregar un elemento al final de la lista.
my_data.append(26047917)
print(f"\nDNI agregado: {my_data}")

# Agregar un elemento en una posición determinada.
my_data.insert(1, "Comolli")
print(f"\nAgregado el apellido: {my_data}")

# Extender la lista con otra lista agregada al final.
my_data.extend(["Cañuelas", "Buenos Aires", "Argentina"])
print(f"\nExtendiendo la lista con datos nuevos:\n{my_data}")

# Eliminar el último elemento de la lista.
my_data.append("Esto se borra")
print(f"\nLista con dato a borrar:\n{my_data}")
my_data.pop()
print(f"Lista con dato borrado:\n{my_data}")
my_data.pop(6)
print(f"El DNI ha sido borrado de la lista:\n{my_data}")

# Eliminar un elemento de la lista pasando su valor.
my_data.remove(46)
print(f"\nLa edad ha sido eliminada:\n{my_data}")

# Ordenar una lista. Si se pasa el parámetro 'reverse=True' ordena al revés.
numbers = [1, 9, 0, 2, 8, 3, 7, 4, 6, 5]
numbers.sort()
print(f"\nSe ordenó la lista de números: {numbers}")
vowels = ["u", "a", "o", "e", "i"]
vowels.sort()
print(f"Se ordenó la lista de letras:{vowels}")

# Invertir los elementos de una lista.
my_data.reverse()
print(f"\nLa lista tiene los datos invertidos:\n{my_data}")
