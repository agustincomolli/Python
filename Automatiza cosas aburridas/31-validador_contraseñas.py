# Valida si un texto pasado cumple con los requisitos de una contraseña 
# fuerte.

from ast import expr
import re

def es_contraseña_fuerte(contraseña):
    """Devuelve True si la contraseña cumple con los requistos:
    8 o más caracteres, mayúsculas y minúsculas y al menos
    un dígito."""

    contraseña = str(contraseña)
    # Chequear si tiene... 
    lista_exp_reg = (r"[\S]{8,}",   # al menos 8 caracteres.
                     r"[A-Z]+",     # al menos una mayúscula.
                     r"[a-z]+",     # al menos una minúscula.
                     r"[\d]+"       # al menos tiene un número.
                    )
    for exp_reg in lista_exp_reg:
        if re.search(exp_reg, contraseña) == None:
            return False
    
    return True


contraseña = input("Ingrese una contraseña: ")
if es_contraseña_fuerte(contraseña):
    print("La contraseña es fuerte.")
else:
    print("No es una contraseña fuerte.")