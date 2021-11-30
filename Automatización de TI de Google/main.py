from sys import path
path.append(".//Módulos")

from module import sumar_Lista, producto_Lista

ceros = [0 for i in range(5)]
unos = [1 for i in range(5)]

print(sumar_Lista(ceros))
print(producto_Lista(unos))
print("Operación realizada con éxito.")