# Para obtener la fecha y hora actuales necesitamos usar la librería
# datetime.
from datetime import datetime
# Para definir un período de tiempo usamos la librería timedelta.
from datetime import timedelta

print("Fechas: \n" + "=" * 7)
# La función now() devuelve un objeto con la fecha y hora actuales.
hoy = datetime.now()
print(f"Hoy es {hoy}")

# Con timedelta() se pueden sumar o restar días o semanas, meses.
un_dia = timedelta(days=1)
ayer = hoy - un_dia
print("Ayer fue " + str(ayer))
una_semana = timedelta(weeks=1)
proxima_semana = hoy + una_semana
print(f"Dentro de una semana será {proxima_semana}")

# Podemos extraer solo una porción de los datos de fechas.
print(f"\nHoy es el día {hoy.day}")
print(f"Este mes es {hoy.month}")
print(f"Este año es {hoy.year}")

cumpleaños = input("¿Cuándo es tu cumpleaños (dd/mm/aa)? ")
fecha_cumpleaños = datetime.strptime(cumpleaños, "%d/%m/%Y")
print(f"Tu cumpleaños es {fecha_cumpleaños}")