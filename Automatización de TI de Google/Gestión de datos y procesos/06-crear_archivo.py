#!/usr/bin/env python3

import os
import sys

nombre_archivo = sys.argv[1]

if not os.path.exists(nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        archivo.write("El archivo nuevo ha sido creado\n")
else:
    print(f"El archivo {nombre_archivo} ya existe.")
    sys.exit(1)