"""
Tu tarea es escribir y probar una función que toma dos argumentos 
(un año y un mes) y devuelve el número de días del mes/año dado (mientras 
que solo febrero es sensible al valor year, tu función debería ser universal).

La parte inicial de la función está lista. Ahora, haz que la función devuelva 
None si los argumentos no tienen sentido.
"""

def is_year_leap(year):
    """
    Description: Devuelve True si el año es bisiesto.
    """

    if year < 1582:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    """
    Description: Devuelve la cantidad de días que tiene un mes.
    """
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
          return 31
    elif month == 2 and is_year_leap(year):
         return 29
    elif month == 2:
         return 28
    else:
         return 30


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
