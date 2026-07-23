print("*** Averiguar cúantos segundos tiene un año dado ***")

year = int(input("\n¿De qué año quiere saber? "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Ese año es bisiesto por lo que tiene un día más.")
    days_year = 366
else:
    days_year = 365

hours_year = days_year * 24
minutes_year = hours_year * 60
seconds_year = minutes_year * 60
print("\nHay", seconds_year, "segundos en ese año.")