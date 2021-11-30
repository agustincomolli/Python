# Prueba: cantidad_semanas
# Escribe una función llamada cantidad_semanas. La función debe tomar un
# argumento, un número entero dias, y devolver una cadena que indique cuántas
# semanas y días son.
# Por ejemplo, llamar a la función e imprimir el resultado de esta manera:

# print(cantidad_semanas(10))
# debería generar lo siguiente:

# 1 week(s) and 3 day(s).

# write your function here
def cantidad_semanas(dias):
    semanas = dias // 7
    dias_restantes = dias % 7
    resultado = f"{semanas} semana(s) y {dias_restantes} día(s)."
    return resultado


# test your function
print(cantidad_semanas(10))
print(cantidad_semanas(1))
print(cantidad_semanas(6))
print(cantidad_semanas(7))
print(cantidad_semanas(9))
print(cantidad_semanas(8042))
