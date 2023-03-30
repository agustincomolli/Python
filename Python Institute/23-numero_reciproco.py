"""
Leer un número natural (un entero no negativo) e imprimir su recíproco. 
De esta forma, 2 se convertirá en 0.5 (1/2) y 4 en 0.25 (1/4)
"""

value = 0
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)
except ValueError:
    print('No se que hacer con', value)
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')
except:
    print('Ha sucedido algo extraño, ¡lo siento!')
