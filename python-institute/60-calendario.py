import locale
import calendar 

locale.setlocale(locale.LC_ALL, "es_AR")

# Para imprimir el calendario se puede usar:
# print(calendar.calendar(2023))
# o bien:
# calendar.prcal(2023)

# Establecer el domingo como primer día de la semana.
calendar.setfirstweekday(calendar.SUNDAY)

calendar.weekheader(4)
calendar.prmonth(2023, 6)

print("\n¿Qué día cae el 10 de junio de 2023?")
day = calendar.day_name[calendar.weekday(2023,6,10)]
print(f"El 10 de junio de 2023 es {day}.")
