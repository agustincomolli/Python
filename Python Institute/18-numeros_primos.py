"""
Escribir una función que verifique si un número es primo o no.
Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 
y si mismo.
"""
def is_prime(num:int):
	"""
	Description: Devuelve True si el argumento es número primo.
	"""

	if num <= 1: # 1 no es número primo.
		return False
	
	# Recorrer los números desde el 2 hasta la raíz cuadrada de num.
	# En cuanto a por qué se suma 1 a la raíz cuadrada del número, es porque 
	# la función range no incluye el límite superior. Por lo tanto, si se 
	# desea iterar hasta el entero más cercano a la raíz cuadrada de num, 
	# debe sumarse 1 al resultado de int(num**0.5).
	for i in range(2, int(num ** 0.5) + 1):
		# Si el num es divisible, terminar y devolver False.
		if num % i == 0:
			return False
	
	return True


for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()