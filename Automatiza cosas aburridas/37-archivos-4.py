import os
from pathlib import Path

win_dir = Path("C:/Windows")
dir_inexistente = Path("C:/este directorio no existe")
calculadora = Path("C:/Windows/System32/calc.exe")
unidad_d = Path("D:/")

print(f"¿Existe el directorio '{win_dir}'? {win_dir.exists()}")
print(f"¿Existe el directorio '{dir_inexistente}'? {dir_inexistente.exists()}")
print(f"¿'{calculadora}' es un archivo? {calculadora.is_file()}")
print(f"¿'{calculadora}' es un directorio? {calculadora.is_dir()}")
print(f"¿Existe el directorio '{unidad_d}'? {unidad_d.exists()}")