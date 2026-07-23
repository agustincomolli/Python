"""
Escribe un script llamado ticket_sla.py que ayude al equipo del Service Desk a 
convertir tiempos de atención de incidencias.

Requerimientos:

1 - Solicitar al usuario:

    - Código de ticket (ej. "INC-4092").

    - Tiempo estimado de resolución en horas (número decimal, ej: 2.5).

2 - Calcular en variables:

    - El tiempo equivalente en minutos.

    - El tiempo equivalente en segundos.

3 - Mostrar la ficha resumen de atención formateada en consola.
"""

print("*** Gestor de Tiempos de Tickets SLA ***")
ticket_code = input("Código de ticket: ")
estimated_hours = float(input("Horas estimadas de resolución: "))
estimated_minutes = estimated_hours * 60
estimated_seconds = estimated_minutes * 60

print(
    "+--------------------------------------------------+\n"
    "                      RESUMEN                       \n"
    "\n"
    f"    Ticket:\t{ticket_code}\n"
    f"    Minutos estimados:\t{estimated_minutes}\n"
    f"    Segundos estimados:\t{estimated_seconds}\n"
    "\n"
    "+--------------------------------------------------+\n"
      )
