from datetime import datetime

my_date = datetime(2020,11,4,14,53,00)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print("Día de la semana:", my_date.strftime("%w"))
print("Día del año:", my_date.strftime("%j"))
print("Número de la semana del año:", my_date.strftime("%U"))