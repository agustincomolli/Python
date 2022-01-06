# Empezar con una lista de usuarios que necesitan ser verificados y con
# una lista vacía de usuarios confirmados.
usuarios_nuevos = ["agustín", "lorena", "adrián"]
usuarios_confirmados = []

# Verificar cada usuario hasta que no queden más usuarios nuevos.
# Mover cada usuario verificado a la lista de usuarios confirmados.
while usuarios_nuevos:
    usuario_actual = usuarios_nuevos.pop()
    print(f"Verificando usuario: {usuario_actual.title()}")
    usuarios_confirmados.append(usuario_actual)

# Mostrar todos los usuarios verificados.
print("\nLos siguentes usuarios han sido verificados: ")
for usuario in usuarios_confirmados:
    print(usuario.title())

# ELiminar todas las instancias de un valor específico en una lista.
mascotas = ["perro", "gato", "perro", "pez", "gato", "conejo", "gato"]
print(mascotas)

while "gato" in mascotas:
    mascotas.remove("gato")

print(mascotas)

# Llenar un diccionario con las entradas del usuario.
respuestas = {}

# Establezca una bandera para indicar que el sondeo está activo.
activo = True

while activo:
    # Solicitar el nombre y la respuesta de la persona.
    nombre = input("\n¿Cuál es su nombre? ")
    respuesta = input("¿Qué montaña te gustaría escalar algún día? ")

    # Almacenar la respuesta en el diccionario.
    respuestas[nombre] = respuesta

    # Averigüar si alguien más participará en la encuesta.
    repetir = input("¿Le gustaría dejar que otra persona responda? (sí | no) ")
    if repetir == "no":
        activo = False

# Encuesta completa, mostrar resultados.
print("\n--- Resultados de la encuesta ---")
for nombre, respuesta in respuestas.items():
    print(f"A {nombre} le gustaría escalar el {respuesta}.")
