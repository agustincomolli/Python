import string
import random

# Incluir en una variable los caracteres válidos para generar
# la contraseña
caracteres = string.ascii_letters
caracteres += string.digits
caracteres += string.punctuation

print("Generador de contraseñas\n" + "=" * 24)
cantidad = int(input("\n¿Cuántas contraseñas deseas crear? "))
longitud = int(input("Longitud de la contraseña: "))
print("Aquí están sus contraseñas: ")
for i in range(cantidad):
    contraseña = ""
    for cantidad in range(longitud):
        contraseña += random.choice(caracteres)
    
    print(contraseña)