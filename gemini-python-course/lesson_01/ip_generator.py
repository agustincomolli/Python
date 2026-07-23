"""
Crea un script que imprima en pantalla la dirección de red, la máscara y el 
gateway de una subred de mantenimiento.

Debes pasar los números por separado (ej. "10", "0", "5", "1") y usar la 
propiedad sep para unirlos con puntos.

El resultado en pantalla debe ser exactamente este:

IP: 10.0.5.50 | Gateway: 10.0.5.1 | Máscara: 255.255.255.0
"""

print("IP: ", end="")
print("10","0","5","50", sep=".", end=" | Gateway: ")
print("10","0","5","1", sep=".", end=" | Máscara: ")
print("255","255","255","0", sep=".")
