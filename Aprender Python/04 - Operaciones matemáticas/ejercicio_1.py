# Usar la función type() para saber el tipo de datos.
print("\nPaso 1: \n********")

print("¿Qué tipo de datos es \"7\"?", type("7"))
print("¿Qué tipo de datos es 7?", type(7))
print("¿Qué tipo de datos es 7.1?", type(7.1),)

# Emplear la función isinstance() para comprobar el tipo de datos.
print("\nPaso 2: \n********")

print("¿\"7\" es string? ", isinstance("7", str))
print("¿7 es integer? ", isinstance(7, int))
print("¿7.1 es float? ", isinstance(7.1, float), "\n")

print("¿7 es string? ", isinstance(7, str))
print("¿\"7\" es integer? ", isinstance("7", int))
print("¿\"7.1\" es float? ", isinstance("7.1", float))