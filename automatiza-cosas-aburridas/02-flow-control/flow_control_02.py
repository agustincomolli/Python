"""
Los fabricantes de discos duros y memorias flash mienten sobre las capacidades 
anunciadas de sus productos usando una definición diferente de TB y GB. Vamos 
a escribir un programa para calcular cuán engañosas son sus capacidades anunciadas. 
"""

import sys

print("Ingrese TB o GB para la unidad anunciada:")
unit = input("> ")

# Calcular la discrepancia que hay en la capacidad anunciada.
if unit == "TB" or unit == "tb":
    discrepancy = 1000000000000 / 1099511627776
elif unit == "GB" or unit == "gb":
    discrepancy = 1000000000 / 1073741824
else:
    print("Debes introducir TB o GB")
    sys.exit()

print("Ingrese la capacidad de la unidad:")
capacity = input("> ")
capacity = float(capacity)

# Calcula la capacidad real,
# redondéala a la centésima más cercana y conviértela en una cadena para que pueda concatenarse:
real_capacity = str(round(capacity * discrepancy, 2))

print("La capacidad real de la unidad es", real_capacity, unit)
