"""
Diseña un banner de consola que simule una alerta de soporte crítico para el 
equipo de infraestructura. Debe verse exactamente con este formato usando un 
único comando print() en tu código:

========================================
[ALERTA] CRITICAL_ERROR: DISK_FULL
========================================
Detalles:
	- Servidor:	PROD-DB-01
	- Espacio:	99% Utilizado
========================================
"""

print(
    "========================================\n"
    "[ALERTA] CRITICAL_ERROR: DISK_FULL\n"
    "========================================\n"
    "Detalles:\n"
    "\t- Servidor:\tPROD-DB-01\n"
    "\t- Espacio:\t99% Utilizado\n"
    "========================================"
)
