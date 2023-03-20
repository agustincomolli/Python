import datetime

# today = datetime.date.today()
# first_day_of_month = today.replace(day=1)
# first_day_of_week = first_day_of_month - datetime.timedelta(days=first_day_of_month.weekday())
# delta = (today - first_day_of_week).days

# if delta % 7 == 0:
#     week_of_month = delta // 7 + 1
# else:
#     week_of_month = delta // 7 + 2

# if week_of_month > 5:
#     week_of_month = 5


today = datetime.date.today()
year, month, day = today.year, today.month, today.day

first_day_of_month = datetime.date(year, month, 1)
first_day_of_month_weekday = first_day_of_month.weekday()

if first_day_of_month_weekday == 6:
    first_day_of_month_weekday = -1

week_of_month = (day + first_day_of_month_weekday) // 7 + 1

print(week_of_month)