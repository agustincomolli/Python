#!/usr/bin/env python3

def frecuencia_caracter(nombre_archivo):
    """Cuenta la frecuencia de cada caracter en un archivo dado."""
    # Primero intentar abrir el archivo.
    try:
        archivo = open(nombre_archivo)
    except OSError:
        return None
    
    # Ahora procesar el archivo.
    caracteres = {}
    for linea in archivo:
        for caracter in linea:
            caracteres[caracter]  = caracteres.get(caracter, 0) + 1
    archivo.close()

    return caracteres