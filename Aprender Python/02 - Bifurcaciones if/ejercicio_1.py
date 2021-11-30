# Bloque de instrucción if
print("\nPrimera parte: \n***************")
valor = "8"

if valor == "7":
    print("El valor es 7")
elif valor == "8":
    print("El valor es 8")
elif valor == "9":
    print("El valor es 9")
else:
    print("El valor no es el que estamos buscando.")

print("Programa completado.")

# Valores superpuestos
print("\nSegunda parte: \n***************")
valor = 6
if valor < 8:
    print("El valor es menor a 8")
elif valor < 7:                         # Esta condición nunca se ejecutará porque si la confición del if
    print("El valor es menor a 7")      # es True también lo será de este elif.
else:
    print("El valor es mayor a 8")

# Bloques if anidados
print("\nTercera parte: \n***************")
primer_valor = True
segundo_valor = "6"

if primer_valor:
    if segundo_valor == "6":
        print("¡Lo tengo!\n")

