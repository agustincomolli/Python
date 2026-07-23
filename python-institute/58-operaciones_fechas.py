import locale
from datetime import datetime
from datetime import date
from datetime import timedelta

my_birthday = date(1977, 6, 10)
today = datetime.now().date()

delta = today - my_birthday

print("Tengo", delta.days, "días de vida.")

print(delta.days // 366, "años")