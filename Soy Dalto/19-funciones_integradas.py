numbers = [4, 7, 42, 15]
print(f"Lista de números:\n{numbers}")

# Buscar el valor más alto.
higher = max(numbers)
print(f"El número más alto es {higher}")

# Buscar el valor más bajo.
lower = min(numbers)
print(f"El número más bajo es {lower}")

# Redondear un número a dos decimales
PI = 3.14159265359
print(f"\nRedondeando PI\n\t{PI}\n\t{round(PI,2)}")

# Comprobar si una variable tiene algún valor que no sea (0, False o None).
my_variable = 1
print(f"\n¿La variable 'my_variable', tiene datos? {bool(my_variable)}")
my_variable = False
print(f"¿La variable 'my_variable', tiene datos? {bool(my_variable)}")

# Comprobar si todos los elementos de un iterable tienen algún valor.
my_list = ["hola", 0, True, "👌"]
print("\n¿Todos los elementos de la lista 'my_list' tienen un valor? " +
      f"{all(my_list)}")


# Sumar todos los números de un iterable.
addition = sum(numbers)
print(f"\nLa suma total de 'numbers' es {addition}")