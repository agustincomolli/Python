"""
Diseña un script que evalúe si la sala de servidores principal debe entrar en 
estado de apagado de emergencia (Emergency Power Off).

Requerimientos:

1 - Solicitar:
    - Temperatura actual en Celsius (float).
    - Estado de los aires acondicionados reduntantes: "OK" o "FALLO" (str).
    - Porcentaje de batería del sistema UPS (float).

2 - Determinar la acción a tomar:
    - APAGADO DE EMERGENCIA: Si la temperatura es mayor a 35.0°C O si el 
      estado del A/C es "FALLO" y la temperatura supera los 28.0°C.
    - ADVERTENCIA DE MANTENIMIENTO: Si el A/C está "OK", la temperatura está 
      entre 24.0°C y 35.0°C, o si la batería del UPS es menor al 20.0%.
    - SISTEMA OPERATIVO OPTIMO: Si la temperatura es menor o igual a 24.0°C, 
      el A/C está "OK" y la batería del UPS es mayor o igual al 20.0%.
"""

print("*** Estado de Apagado de Emergencia ***\n")

actual_temp = float(input("Temperatura actual: "))
air_conditioning = input("Aires acondicionados [OK | FALLO]: ")
ups_battery = float(input("Porcentaje batería UPS: "))

if (actual_temp > 35.0) or (air_conditioning == "FALLO" and actual_temp > 28.0):
    print("\nAPAGADO DE EMERGENCIA")
elif (air_conditioning == "OK" and 24.0 <= actual_temp <= 35.0) or (ups_battery < 20.0):
    print("\nADVERTENCIA DE MANTENIMIENTO")
else:
    print("\nSISTEMA OPERATIVO OPTIMO")
