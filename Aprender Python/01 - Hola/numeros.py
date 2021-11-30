# Crear un programa que solicita al usuario final dos valores, los 
# suma y muestra los resultados.

print("Primer número: ")
# La función input() devuelve en forma de cadena la entrada del usuario.
# La función int() convierte una cadena en número entero.
numero_1 = int(input())
print("Segundo número: ")
numero_2 = int(input())
suma = numero_1 + numero_2
# La función str() convierte un número en una cadena.
print("La suma es: " + str(suma))