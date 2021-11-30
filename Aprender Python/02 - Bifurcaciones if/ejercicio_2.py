# Tipos de datos.
print("\nPrimera parte: \n***************")

print(type("¡Hola mundo!")) # Cadena
print(type(7))              # Número entero

print(type(True))           # Valor booleano
print(type(False))          # Valor booleano

print(type("True"))         # Cadena
print(type("False"))        # Cadena

# Covertir cadenas en booleanos.
print("\nSegunda parte: \n***************")

print(bool("True"))         # True
print(bool("False"))        # False
print(bool(""))             # True
print(bool(" "))            # True
print(bool("¡Hola mundo!")) # True

# Covertir enteros en booleanos.
print("\nTercera parte: \n***************")

print(bool(7))  # True
print(bool(1))  # True
print(bool(0))  # False
print(bool(-1)) # True

# Expresiones booleanas.
print("\nCuarta parte: \n**************")

print(1 + 1 == 3)   # False
print(1 + 1 == 2)   # True

# Operadores de comparación.
print("\nQuinta parte: \n**************")

print(3 == 4)   # False
print(3 != 4)   # True

print(3 > 4)    # False
print(3 < 4)    # True
print(3 >= 4)   # False
print(3 <= 4)   # True

# Operadores lógicos.
print("\nSexta parte: \n*************")

primer_numero = 5
segundo_numero = 0
valor_verdadero = True
valor_falso = False

if primer_numero > 1 and primer_numero < 10:
    print("El valor está entre 1 y 10.")

if primer_numero > 1 or segundo_numero > 1:
    print("Al menos un de los valores es mayor a 1.")

print(not valor_verdadero)
print(not valor_falso)

if not primer_numero > 1 and segundo_numero < 10:
    print("Ambos valores pasaron la prueba")
else:
    print("Ambos valores NO pasaron la prueba")