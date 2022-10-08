"""  
Magic 8 Ball es un juguete de oficina popular y un juguete para niños inventado en la década de 1940 para adivinar y buscar consejos. 🎱

Es una bola 8 de gran tamaño con algunas de las siguientes respuestas:

Sí definitivamente.
Es decididamente así.
Sin duda.
Respuesta confusa, intenta otra vez.
Pregunta de nuevo más tarde.
Mejor no decirte ahora.
Mis fuentes dicen que no.
Las perspectivas no son tan buenas.
Muy dudoso

Cree un programa magic8.py que pueda responder cualquier pregunta de Sí o No con una fortuna/consejo diferente cada vez que se ejecute. 

"""

import random

print("Magic 8 Ball 🎱\n")

question = input("Pregunta: ")

# Generar la respuesta aleatoria.
answer = random.randint(1,9)

if answer == 1:
    print("Magic 8 Ball: Sí definitivamente.")
elif answer == 2:
    print("Magic 8 Ball: Es decididamente así.")
elif answer == 3:
    print("Magic 8 Ball: Sin duda.")
elif answer == 4:
    print("Magic 8 Ball: Respuesta confusa, intenta otra vez.")
elif answer == 5:
    print("Magic 8 Ball: Pregunta de nuevo más tarde.")
elif answer == 6:
    print("Magic 8 Ball: Mejor no decirte ahora.")
elif answer == 7:
    print("Magic 8 Ball: Mis fuentes dicen que no.")
elif answer == 8:
    print("Magic 8 Ball: Las perspectivas no son tan buenas.")
elif answer == 8:
    print("Magic 8 Ball: Muy dudoso")
else:
    print("Error")