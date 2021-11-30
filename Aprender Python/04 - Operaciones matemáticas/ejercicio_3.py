# Realizar varias operaciones matemáticas.
print("\nPaso 1: \n********")

primer_valor = 5
segundo_valor = 4

suma = primer_valor + segundo_valor
resta = primer_valor - segundo_valor
multiplicacion = primer_valor * segundo_valor
division = primer_valor / segundo_valor
modulo = primer_valor % segundo_valor
potencia = primer_valor ** segundo_valor

print("Suma: " + str(suma))
print("Resta: " + str(resta))
print("Multiplicación: " + str(multiplicacion))
print("División: " + str(division))
print("Módulo: " + str(modulo))
print("Potencia: " + str(potencia))

# Controlar el orden predeterminado de las operaciones.
print("\nPaso 2: \n********")

print(3 + 4 * 5)
print((3 + 4) * 5)

# Investigar la división más detenidamente.
print("\nPaso 3: \n********")

dividendo = 5
divisor = 4
cociente = dividendo / divisor

print(type(cociente))
print(cociente)

# Convertir float en int.
print("\nPaso 4: \n********")

pi = 3.14
print(type(pi))
print(int(pi))
print(round(pi)) # La función round() ofrece una manera de hacer el redondeo.

uptime = 99.99
print(type(uptime))
print(int(uptime))
print(round(uptime))

# Redondear a una posición decimal específica.
print("\nPaso 5: \n********")

primer_valor = round(7.654321, 2)
print(primer_valor)

segundo_valor = round(9.87654, 3)
print(segundo_valor)