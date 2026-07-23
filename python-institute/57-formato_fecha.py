import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, "es_AR")

today = datetime.strftime(datetime.now(), "%d de %B de %Y")
print(f"Hoy es {today}")

my_date = datetime.strptime(today, "%d de %B de %Y")
print(my_date)