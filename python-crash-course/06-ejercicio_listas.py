print("¡Bienvenidos a mi cumpleaños!\n" + "*" * 29)
# Crear lista de invitados.
invitados = ["Adrián", "Gabriel", "Carlitos"]

# Realizar las invitaciones.
print("Hola " + invitados[0] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[1] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[2] + " estás invitado a mi cumpleaños.\n")
print("Hemos invitado a " + str(len(invitados)) + " personas.\n")

# Gabriel no puede ir, invitar a Gustavo.
print(invitados[1] + " no puede asistir al evento.\n")
invitados[1] = "Gustavo"

# Realizar las invitaciones nuevamente.
print("Hola " + invitados[0] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[1] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[2] + " estás invitado a mi cumpleaños.\n")
print("Hemos invitado a " + str(len(invitados)) + " personas.\n")

# Invitar a más personas.
print("¡Invitamos a más personas!")
invitados.insert(0, "Raúl")
invitados.insert(2, "Facundo")
invitados.append("Luís María")

# Realizar las invitaciones nuevamente.
print("Hola " + invitados[0] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[1] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[2] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[3] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[4] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[5] + " estás invitado a mi cumpleaños.\n")
print("Hemos invitado a " + str(len(invitados)) + " personas.\n")

# Dejar sólo a dos invitados.
print("¡Ufa, ahora solo puedo invitar a dos personas!")
print(invitados.pop() + " perdón pero no puedo invitarte esta vez.")
print(invitados.pop(3) + " perdón pero no puedo invitarte esta vez.")
print(invitados.pop(2) + " perdón pero no puedo invitarte esta vez.")
print(invitados.pop(0) + " perdón pero no puedo invitarte esta vez.\n")
print("Hola " + invitados[0] + " estás invitado a mi cumpleaños.")
print("Hola " + invitados[1] + " estás invitado a mi cumpleaños.")

# Limpiar la lista.
del invitados[1]
del invitados[0]
print("\nLista de invitados limpia: " + str(invitados))