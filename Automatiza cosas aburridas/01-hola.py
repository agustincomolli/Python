# Este programa me saluda y me pide mi nombre.

print("¡Hola mundo!")

print("¿Cuál es tu nombre? ") # preguntar por su nombre.
mi_nombre = input()
print("¡Un placer conocerte " + mi_nombre + "!")

print("La longitud de tu nombre es de: ")
print(len(mi_nombre))

print("¿Cuál es tu edad? ") # preguntar por su edad.
mi_edad = input()
print("Usted tendrá " + str(int(mi_edad) + 1) + " en un año.")