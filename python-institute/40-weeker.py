"""
Tu tarea es implementar una clase llamada Weeker. Sí, tus ojos no te engañan, 
este nombre proviene del hecho de que los objetos de esta clase podrán 
almacenar y manipular los días de la semana.

El constructor de la clase acepta un argumento: una cadena. La cadena 
representa el nombre del día de la semana y los únicos valores aceptables 
deben provenir del siguiente conjunto:

Lun Mar Mie Jue Vie Sab Dom

Invocar al constructor con un argumento desde fuera de este conjunto debería 
generar la excepción WeekDayError (defínela tu mismo; no te preocupes, pronto 
hablaremos sobre la naturaleza objetiva de las excepciones). La clase debe 
proporcionar las siguientes facilidades:

- Los objetos de la clase deben ser "imprimibles", es decir, deben poder 
convertirse implícitamente en cadenas de la misma forma que los argumentos 
del constructor.
- La clase debe estar equipada con métodos de un parámetro llamados 
add_days(n) y subtract_days(n), siendo n un número entero que actualiza el día 
de la semana almacenado dentro del objeto mediante el número de días indicado, 
hacia adelante o hacia atrás.
- Todas las propiedades del objeto deben ser privadas.

"""


class WeekDayError(Exception):
    def __init__(self):
        super().__init__("Oops, you screwed up!")


class Weeker:
    __weekdays = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

    def __init__(self, day):
        if day not in self.__weekdays:
            raise WeekDayError
        
        self.__day = self.__weekdays.index(day)
        print(self.__day)

    def __str__(self):
        return self.__weekdays[self.__day]

    def add_days(self, n):
        print(self.__day)
        self.__day = (self.__day + n) % 7

    def subtract_days(self, n):
        self.__day = (self.__day - n) % 7


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lun1')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
