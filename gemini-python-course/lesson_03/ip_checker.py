"""
Crea un script que valide la sintaxis básica de los 4 octetos de una IPv4 
ingresada por un técnico de soporte.

Requerimientos:

1 - Solicitar los 4 octetos por separado como enteros (octeto_1, octeto_2, 
    octeto_3, octeto_4).
2 - Validar que todos y cada uno de los octetos estén en el rango de 0 a 
    255 (inclusive).
3 - Validar reglas de arquitectura de red:
    - Si el octeto_1 es igual a 127, mostrar: "Dirección de Loopback 
      (Reservada)".
    - Si todos los octetos están en el rango válido (0 a 255) y no es 
      Loopback, mostrar: "Dirección IP Válida: 
      <octeto_1>.<octeto_2>.<octeto_3>.<octeto_4>".
    - Si al menos uno de los octetos está fuera del rango (menor a 0 o 
      mayor a 255), mostrar: "ERROR: Uno o más octetos no son válidos 
      (deben estar entre 0 y 255)".
"""

octet_1 = int(input("Octeto 1: "))
octet_2 = int(input("Octeto 2: "))
octet_3 = int(input("Octeto 3: "))
octet_4 = int(input("Octeto 4: "))

is_valid = (0 <= octet_1 <= 255) and (0 <= octet_2 <= 255)
is_valid = (is_valid) and (0 <= octet_3 <= 255) and (0 <= octet_4 <= 255)

if not is_valid:
    print("ERROR: Uno o más octetos no son válidos (deben estar entre 0 y 255)")
elif octet_1 == 127:
    print("Dirección de Loopback (Reservada)")
else:
    print(f"Dirección IP Válida: {octet_1}.{octet_2}.{octet_3}.{octet_4}")
