"""
Ejemplo de sentencia break y continue en un bucle.
"""

while True:
    print("¿Quién eres?")
    name = input("> ")
    if name != "Juan":
        continue
    print("¡Hola, Juan! ¿Cuál es tu contraseña? (es un 🐟)")
    password = input("> ")
    if password == "pejerrey":
        break

print("Acceso concedido.")
