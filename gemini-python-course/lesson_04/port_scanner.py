"""
Escribe un script que simule el escaneo de un rango de puertos en un servidor objetivo.

Requerimientos:

1 - Solicitar por consola:
    * Puerto inicial (int).
    * Puerto final (int).

2 - Utilizar un bucle for con range() para recorrer desde el puerto inicial hasta el 
puerto final (inclusive).

3 - Para cada puerto:
    * Si el puerto es el 22, 80 o 443, imprimir: [ABIERTO] Puerto <puerto>: Servicio 
    crítico activo.
    * Para cualquier otro puerto, imprimir: [CERRADO] Puerto <puerto>.
"""

initial_port = int(input("Puerto inicial: "))
final_port = int(input("Puerto final: "))

print()
for i in range(initial_port, final_port + 1):
    if i == 22 or i == 80 or i == 443:
        print(f"[ABIERTO] Puerto {i}: Servicio crítico activo.")
    else:
        print(f"[CERRADO] Puerto {i}")
