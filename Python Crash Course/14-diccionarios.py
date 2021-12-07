# Definir un diccionario con dos claves-valor.
# alien_0 = {"color" : "verde", "puntos" : 5}
print("\nDiccionarios:")
alien_0 = {}
alien_0["color"] = "verde"
alien_0["puntos"] = 5

print("Color: " + alien_0["color"])
print("Puntos: " + str(alien_0["puntos"]))

# Agregar nuevas claves-valor al diccionario.
alien_0["posicion-x"] = 0
alien_0["posicion-y"] = 25

print(alien_0)

# Cambiar valores al diccionario.
print("\nEl alien es " + alien_0["color"])
alien_0["color"] = "amarillo"
print("El alien ahora es " + alien_0["color"])

# Mover el alien a la derecha.
# Considerar que tan lejos moverlo, basado en la velocidad actual.
alien_0["velocidad"] = "media"
print("\nLa posición original es " + str(alien_0["posicion-x"]))
if alien_0["velocidad"] == "lenta":
    incrementar_x = 1
elif alien_0["velocidad"] == "media":
    incrementar_x = 2
else:
    incrementar_x = 3
# La nueva posición es la anterior + el incremento.
alien_0["posicion-x"] += incrementar_x
print("La nueva posición es " + str(alien_0["posicion-x"]))

# Borrar una clave-valor.
del alien_0["puntos"]
print("\nClave 'puntos' borrada: " + str(alien_0))
