from random import choice
import string

def generar_contraseña(longitud):
    contraseña = ""
    caracteres = string.ascii_letters + string.digits + "@-_+."
    for i in range(longitud):
        contraseña += choice(caracteres)
    
    return contraseña

print(generar_contraseña(8))