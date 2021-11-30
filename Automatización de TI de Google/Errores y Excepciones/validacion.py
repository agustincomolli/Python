#!/usr/bin/env python3

def validar_usuario(nombre_usuario, minlen):
    assert type(nombre_usuario) == str, "El nombre de usuario debe ser un string."
    if minlen < 1:
        raise ValueError("minlen debe tener al menos el valor de 1")
    if len(nombre_usuario) < minlen:
        return False
    if not nombre_usuario.isalnum():
        return False
    
    return True

# validar_usuario("miusuario")    # TypeError: validar_usuario() missing 1 required positional argument: 'minlen'
# validar_usuario("miusuario", 1)
# validar_usuario(88, 1)            # AssertionError: El nombre de usuario debe ser un string.
# validar_usuario(["misuario"], 1)  # AssertionError: El nombre de usuario debe ser un string.