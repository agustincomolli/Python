import re
import os

# Lista de aplicaciones a excluir de las actualizaciones
exclusion_list = ["VMware.WorkstationPro"]

# Ejecutar el comando 'winget update' y obtener la salida
output = os.popen('winget update').read()

# Patrón para encontrar identificadores de aplicaciones en la salida
pattern = re.compile(r"(\w+\.[^\s]+)")
ids = re.findall(pattern, output)

# Iterar sobre los identificadores encontrados
for id in ids:
    # Verificar si el identificador no es numérico y no está en la lista de exclusión
    if not id[0].isnumeric() and id not in exclusion_list:
        # Imprimir mensaje de actualización
        print(f"Actualizando {id}")
        
        # Ejecutar el comando 'winget upgrade' para actualizar la aplicación
        os.system(f"winget upgrade {id}")
