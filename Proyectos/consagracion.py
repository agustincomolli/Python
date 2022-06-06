# Este script devuelve a partir de una fecha de una festividad de María,
# que se utilizará para hacer la consagración total como su esclavo, la
# fecha inicial para empezar el método de los 33 días de san Luís María
# Grignon de Montfort.

from asyncio import as_completed
from datetime import datetime
from datetime import timedelta

def obtener_fecha_inicial(fecha_consagracion):
    """Dada una cadena que contiene la fecha de consagración, se restarán
       34 días para obtener la fecha de inicio."""

    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
             "julio", "agosto", "septiembre", "octubre", "noviembre", 
             "diciembre")

    fecha_consagracion = datetime.strptime(fecha_consagracion, "%d-%m")
    fecha_inicio = fecha_consagracion - timedelta(days=34)
    # fecha_inicio = datetime.strftime(fecha_inicio, "%d-%m")
    fecha_inicio = f"{fecha_inicio.day} de {meses[fecha_inicio.month -1]}"
    return  fecha_inicio

print("Consagración a la Virgen".center(65))
print(f"{'*'*26}".center(65))
fecha_consagracion = input("\nIngrese la fecha de consagración [dd-mm]: ")

try:
    fecha_inicio = obtener_fecha_inicial(fecha_consagracion)
except ValueError:
    print("ERROR: Debe ingresar una fecha con el formato válido: \"dd-mm\"")
    exit()

print(f"La fecha de inicio para la preparación es el: \"{fecha_inicio}\"")