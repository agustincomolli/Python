import os

def leer_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return ""
    if not os.path.isfile(nombre_archivo):
        return ""
    if not os.access(nombre_archivo, os.R_OK):
        return ""
    