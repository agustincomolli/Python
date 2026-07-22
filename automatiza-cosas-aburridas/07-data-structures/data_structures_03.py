"""
Devolviendo claves y valores. Tres métodos: keys(), values(), items()
"""

things = {"color": "verde", "number": 10, "animal": "perro"}

print("Estas son las claves del diccionario:")
# Para recuperar las claves ya no hace falta usar el método keys().
for key in things:
    print(key, end=" ")

print()
print("Estos son los valores:")
for value in things.values():
    print(value, end=" ")

print()
print("Estos son los items (clave-valor):")
for key, value in things.items():
    print(key + ":" + str(value), end=" ")

print()
# Recuperar un valor y usar un valor de respaldo por si la clave no existe.
print("El mejor libro es: " + str(things.get("libro", "Martín Fierro")))
