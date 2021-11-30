# Creación de una lista de valores
print("\nPaso 1: \n********")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "marrón"]

print(colores)
print(type(colores))

datos_diversos = ["Juan", 3.14, 7, False]

print(datos_diversos)
print(type(datos_diversos))

# Acceder a elementos individuales.
print("\nPaso 2: \n********")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "marrón"]

print(f"Indexación basada en 0... segundo elemento en la lista: {colores[1]}")
print(f"Último elemento de la lista: {colores[-1]}")
print(f"Ante último elemento de la lista: {colores[-2]}")

# Crear de un segmento
print("\nPaso 3: \n********")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "marrón"]

print("\nImprima un segmento, comenzando en el índice 2 y excluyendo el índice 5: ")
print(colores[2:5])
print(type(colores[2:5]))

print("\ nImprimir un segmento, comenzando en el índice 0 hasta el índice 3:")
print(colores[:3])

print("\ nImprime un segmento, comenzando un índice 4 hasta el final de la lista:")
print(colores[4:])

print("\ nImprimir un corte, desde el cuarto desde el final (pero no el último elemento):")
print(colores[-4:-1])

# Inversión y ordenación de la lista.
print("\nPaso 3: \n********")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "marrón"]

colores.reverse()
print(colores)

colores.sort()
print(colores)

# Tratar la lista como una cola
print("\nPaso 4: \n********")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "marrón"]

print(colores)
color = colores.pop(0)

print("Color eliminado: ", color)
print(colores)

# Agregar o eliminar elementos a una lista
print("\nPaso 5: \n********")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "marrón"]

print(colores)

colores.append("blanco")
colores.append("negro")

colores.remove("amarillo")
colores.remove("naranja")

print(colores)

# Combinar una lista nueva con una existente.
print("\nPaso 6: \n********")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "marrón"]
nuevos_colores = ["celeste", "gris"]

colores.extend(nuevos_colores)

print(colores)

# Borrar todos los elementos de una lista.
print("\nPaso 6: \n********")

colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "marrón"]

print(colores)
colores.clear() # El método clear() borra todos los elementos de la lista.
print(colores)