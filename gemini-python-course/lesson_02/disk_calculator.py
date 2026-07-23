"""
Crea un script llamado disk_calculator.py que solicite datos al administrador 
de sistemas para calcular la capacidad de almacenamiento disponible en un 
servidor NAS.

Requerimientos:

1 - Solicitar por consola:

    * Nombre del servidor (texto).

    * Capacidad total del disco en GB (número decimal).

    * Espacio libre actual en GB (número decimal).

2 - Calcular en variables separadas:

    * Espacio utilizado en GB.

    * Porcentaje de espacio libre respecto al total.

3 - Imprimir el siguiente reporte en pantalla usando f-strings y tabulaciones \t:

========================================
	REPORTE DE ALMACENAMIENTO NAS
========================================
Servidor Evaluado:	<nombre_del_servidor>
Capacidad Total:	<total> GB
Espacio Utilizado:	<utilizado> GB
Porcentaje Libre:	<porcentaje>%
========================================
"""

name_server = input("Servidor Evaluado: ")
total_capacity = float(input("Capacidad Total: "))
free_space = float(input("Espacio Libre: "))

used_space = total_capacity - free_space
free_percentage = (free_space * 100) / total_capacity

print(
"========================================\n"
"\tREPORTE DE ALMACENAMIENTO NAS\n"
"========================================\n"
f"Servidor Evaluado:\t{name_server}\n"
f"Capacidad Total:\t{total_capacity} GB\n"
f"Espacio Utilizado:\t{used_space} GB\n"
f"Porcentaje Libre:\t{free_percentage}%\n"
"========================================"
)
