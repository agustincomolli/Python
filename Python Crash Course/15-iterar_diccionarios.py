usuario_0 = {
    "nombre_usuario" : "agustincomolli",
    "nombre" : "agustín",
    "apellido" : "comolli"
    }

# Iterar por el diccionario.
for clave, valor in usuario_0.items():
    print("\nClave: " + clave)
    print("Valor: " + valor)

lenguajes_favoritos = {
    "Agustín" : "Python",
    "Lorena" : "JavaScript",
    "Gustavo" : "Visual Basic",
    "Fernanda" : "FoxPro",
    "Carlitos" : "Clipper",
    "Miguel" : "C++",
    "Adrián" : "Python"
}

print("\nLenguajes favoritos:")
for nombre, lenguaje in lenguajes_favoritos.items():
    print(f"El lenguaje favorito de {nombre} es {lenguaje}.")

# Iterar diccionario solo por las claves.
amigos = ["Gustavo", "Carlitos"]
for nombre in lenguajes_favoritos.keys():
    print(nombre)
    if nombre in amigos:
        print("Hola " + nombre + " veo que tu lenguaje favorito es " +
            lenguajes_favoritos[nombre] + ".")

# Ordenar la salida.
print("\nLista ordenada:")
for nombre in sorted(lenguajes_favoritos.keys()):
    print(nombre + " gracias por completar la encuesta.")

# Iterar diccionario por su valor. La función set() elimina los duplicados.
print("\nLos siguentes lenguajes están en el diccionario:")
for lenguaje in set(lenguajes_favoritos.values()):
    print(lenguaje)