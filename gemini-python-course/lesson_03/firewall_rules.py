"""
Sistema de Triaje de Severidad de Firewall (firewall_rules.py)
Escribe un script que clasifique un evento de red capturado por el firewall.

Requerimientos:

1 - Solicitar al usuario:
    a - Puerto de destino (entero).
    b - Intentos fallidos de conexión (entero).

2 - Determinar el nivel de amenaza bajo las siguientes reglas:
    a - ALTA AMENAZA: Si el puerto es 22 (SSH) o 3389 (RDP) Y los intentos 
    fallidos son mayores o iguales a 5.
    b - ALERTA MEDIA: Si los intentos fallidos son mayores o iguales a 10 
    (independientemente del puerto).
    c - TRÁFICO NORMAL: Cualquier otro caso.

3 - Imprimir el resultado indicando el nivel de amenaza asignado.
"""

destination_port = int(input("Puerto de destino: "))
failed_attempts = int(input("Intentos fallidos de conexión: "))

if (destination_port == 22 or destination_port == 3389) and failed_attempts >= 5:
    print("ALTA AMENAZA")
elif failed_attempts >= 10:
    print("ALERTA MEDIA")
else:
    print("TRAFICO NORMAL")
