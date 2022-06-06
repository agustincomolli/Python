import random

def saludar(nombre):
    """Imprimir un saludo con el nombre."""
    print(f"¡Hola {nombre}!")


saludar("Agustín")
saludar("Lorena")

def obtener_respuesta(numero_respuesta):
    """Devuelve un mensaje según el número dado."""
    if numero_respuesta == 1:
        return "Es cierto."
    elif numero_respuesta == 2:
        return "Decididamente es así."
    elif numero_respuesta == 3:
        return "Sí."
    elif numero_respuesta == 4:
        return "Respuesta confusa, inténtalo de nuevo."
    elif numero_respuesta == 5:
        return "Responde de nuevo más tarde."
    elif numero_respuesta == 6:
        return "Concéntrate y responde de nuevo."
    elif numero_respuesta == 7:
        return "Mi respuesta es no."
    elif numero_respuesta == 8:
        return "Las perspectivas no son tan buenas."
    elif numero_respuesta == 9:
        return "Muy dudoso."
    

numero = random.randint(1, 10)
respuesta = obtener_respuesta(numero)
print(respuesta)