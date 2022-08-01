#!/usr/bin/env python3
# Copia una carpeta completa y su contenido en un archivo zip y el nombre del
# archivo se incrementa.

import zipfile
import os

def backup_to_zip(folder):
    """
        DESCRIPCIÓN: Copia el contenido de una carpeta en un archivo zip.
        PARÁMETROS:
            - folder: Es la ruta de la carpeta a copiar.
    """
    # Asegurarse de que la ruta sea absoluta.
    folder = os.path.abspath(folder) 
    
    # Averiguar qué nombre de archivo usar según los archivos existentes.
    number = 0
    while True:
        zip_file = os.path.basename(folder) + "_" + number + ".zip"
        if not os.path.exists(zip_file):
            break
        number += 1