from modulo_encuesta import Encuesta_Anonima

# Definir la pregunta y crear la encuesta.
pregunta = "¿Qué idioma aprendiste a hablar primero?"
encuesta = Encuesta_Anonima(pregunta)

# Mostrar la pregunta y guardar las respuestas.
encuesta.mostrar_pregunta()
print("Ingrese 's' para terminar en cualquier momento.\n")
while True:
    respuesta = input("Idioma: ")
    if respuesta == "s":
        break
    encuesta.guardar_respuesta(respuesta)

# Mostrar los resultados de la encuesta.
print("\n¡Muchas gracias a todos los que participaron de la encuesta!")
encuesta.mostrar_resultados()