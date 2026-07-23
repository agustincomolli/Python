import string

# Encriptar un mensaje usando el cifrado Cesar.
def encriptar_mensaje(mensaje, clave):
    caracteres = string.ascii_letters + "áéíóú"
    mensaje_encriptado = ""
    for caracter in mensaje:
        if caracter in caracteres:
            posicion = caracteres.find(caracter)
            # Si la nueva posición supera la cantidad de caracteres, debe volver
            # a empezar en 0.
            nueva_posicion = (posicion + clave) % len(caracteres)
            mensaje_encriptado += caracteres[nueva_posicion]
        else:
            mensaje_encriptado += caracter
    return mensaje_encriptado


# Desencriptar un mensaje encriptado con el cifrado Cesar.
def desencriptar_mensaje(mensaje, clave):
    caracteres = string.ascii_letters + "áéíóú"
    mensaje_desencriptado = ""
    for caracter in mensaje:
        if caracter in caracteres:
            posicion = caracteres.find(caracter)
            # Si la nueva posición supera la cantidad de caracteres, debe volver
            # a empezar en 0.
            nueva_posicion = (posicion - clave) % len(caracteres)
            mensaje_desencriptado += caracteres[nueva_posicion]
        else:
            mensaje_desencriptado += caracter
    return mensaje_desencriptado


print(f"Generador de mensajes secretos\n" + "=" * 30)
mensaje = input("\nIntroduce un mensaje: ")
clave = 3
encriptado = encriptar_mensaje(mensaje, 3)
print(f"El mensaje encriptado es: \"{encriptado}\"")
desencriptado = desencriptar_mensaje(encriptado, 3)
print(f"El mensaje original era: {desencriptado}")