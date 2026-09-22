"""
Ejercicio 3: Calculador de Rango de Barrido de Red (Dificultad: Avanzada)
Diseña un script llamado ip_range.py que calcule el alcance de un escaneo 
de puertos en un segmento de red.

Requerimientos:

Solicitar al usuario:

Los primeros tres octetos de la red (ej. "10.20.1").

Octeto del host inicial (ej. 10).

Octeto del host final (ej. 55).

Calcular:

La cantidad total de IPs que se van a escanear en ese rango.

Imprimir la IP de inicio, la IP de fin y el total de hosts a analizar.

Restricción técnica: Para construir la IP de inicio y fin dentro del reporte, 
debes usar obligatoriamente el parámetro sep="." dentro de un llamado print() 
o la combinación de variables vistas.

--- CONFIGURACIÓN DE BARRIDO DE RED ---
Rango a escanear: 10.20.1.10 -> 10.20.1.55
Total de direcciones IP objetivo: 46
"""

print("*** Calculador de Rango de Barrido de Red ***")
print("\nIngrese los primeros tres octetos de la red (ej. '10.20.1')")
first_octets_network = input("> ")
print("Octeto del host inicial (ej. 10).")
initial_host = input("> ")
print("Octeto del host final (ej. 55).")
final_host = input("> ")

INITIAL_IP = f"{first_octets_network}.{initial_host}"
FINAL_IP = f"{first_octets_network}.{final_host}"
# +1 para incluir tanto la IP inicial como la final en el rango de escaneo
total_hosts = int(final_host) - int(initial_host) + 1

print("\n--- CONFIGURACIÓN DE BARRIDO DE RED ---")
print(f"Rango a escanear: {INITIAL_IP} -> {FINAL_IP}")
print(f"Total de direcciones IP objetivo: {total_hosts}")
