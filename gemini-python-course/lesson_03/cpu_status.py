"""
Ejemplo de estructuras condicionales.
"""

cpu_usage = float(input("Uso de CPU (%): "))

if cpu_usage >= 90:
    print("[CRITICO] CPU saturada. Enviando alerta...")
elif cpu_usage >= 70:
    print("[ADVERTENCIA] Uso elevado de CPU.")
else:
    print("[OK] Estado del sistema normal.")
