"""
Tu tarea ahora es ampliar su funcionalidad con un nuevo método llamado 
count_weekday_in_year, que toma un año y un día de la semana como parámetros, 
y luego devuelve el número de ocurrencias de un día de la semana específico 
en el año.

Utiliza los siguientes consejos:

- Crea una clase llamada MyCalendar que se extiende de la clase Calendar.
- Crea el método count_weekday_in_year con los parámetros de year y weekday. 
El parámetro weekday debe tener un valor entre 0 y 6, donde 0 es el Lunes y 6 
es el Domingo. El método debe devolver el número de días como un número entero.
- En tu implementación, usa el método monthdays2calendar de la clase Calendar.

"""

import calendar


class MyCalendar(calendar.Calendar):

    def __init__(self, firstweekday: int = 0) -> None:
        super().__init__(firstweekday)

    def count_weekday_in_year(self, year: int, weekday: int) -> int:
        try:
            if weekday < 0 or weekday > 6:
                raise ValueError
        except ValueError as error:
            print("El día de la semana debe ser entre 0 y 6.")
            return
        
        count = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for day, num_day in week:
                    if num_day == weekday and day != 0:
                        count += 1

        return count


my_calendar = MyCalendar()
count_day = my_calendar.count_weekday_in_year(2000, 6)
print(count_day)