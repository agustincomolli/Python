"""
Tu tarea es escribir y probar una función que toma tres argumentos (un año, 
un mes y un día del mes) y devuelve el día correspondiente del año, o 
devuelve None si cualquiera de los argumentos no es válido.
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


def day_of_year(year, month, day):
    """
    Description: Devuelve el día correspondiente del año para una fecha dada.
    """

    if year < 1582 or month < 1 or month > 12 or day < 1 or day > 31:
        # Fecha inválida.
        return None
    elif month == 2 and day == 29 and not is_year_leap(year):
        # El año no es bisiesto por lo tanto no puede tener 29 días.
        return None
    
    days = day
    # Recorrer los meses hasta el actual y sumar la cantidad de sus días.
    for i in range(1, month):
        days += days_in_month(year, i)

    return days


print(day_of_year(2000, 12, 31))
print(day_of_year(1986, 2, 29))
print(day_of_year(1988, 2, 29))
print(day_of_year(1977, 6, 10))
print(day_of_year(1941, 3, 10))
