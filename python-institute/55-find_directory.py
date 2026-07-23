"""
Tu programa debe cumplir con los siguientes requisitos:

- Escribe una función o método llamado find que tome dos argumentos llamados 
path y dir. El argumento path debe aceptar una ruta relativa o absoluta a un 
directorio donde debe comenzar la búsqueda, mientras que el argumento dir debe 
ser el nombre de un directorio en el que deseas encontrar la ruta dada. Tu 
programa debería mostrar las rutas absolutas si encuentra un directorio con el 
nombre dado.
- La búsqueda en el directorio debe realizarse de forma recursiva. Esto 
significa que la búsqueda también debe incluir todos los subdirectorios en la 
ruta dada.

"""

import my_os_lib as mol
import os


def find(path: str, dir: str):
    try:
        mol.cd(path)
    except OSError:
        return
    
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        if item == dir:
            print(os.path.join(current_dir, item))
        
        find(os.path.join(current_dir,item), dir)


find("./tree", "06-bisiesto.py")
