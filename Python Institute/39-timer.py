"""
Tu clase se llamará Timer (temporizador en español). Su constructor acepta tres
argumentos que representan horas (un valor del rango [0..23]; usaremos tiempo 
militar), minutos (del rango [0. .59]) y segundos (del rango [0..59]).

Cero es el valor predeterminado para todos los parámetros anteriores. No es 
necesario realizar ninguna comprobación de validación.

La clase en sí debería proporcionar las siguientes facilidades:
- Los objetos de la clase deben ser "imprimibles", es decir, deben poder 
convertirse implícitamente en cadenas de la siguiente forma: "hh:mm:ss", 
con ceros a la izquierda agregados cuando cualquiera de los valores es menor 
que 10.
- La clase debe estar equipada con métodos sin parámetros llamados next_second() 
y previous_second (), incrementando el tiempo almacenado dentro de los objetos 
en +1/-1 segundos respectivamente.

Emplea las siguientes sugerencias:
- Todas las propiedades del objeto deben ser privadas.
- Considera escribir una función separada (¡no un método!) para formatear la 
cadena con el tiempo.

"""

class Timer:
    def __init__(self, hour=0, minutes=0, seconds=0):
        self.__hour = hour
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        time = ""
        if self.__hour < 10:
            time += "0" + str(self.__hour)
        else:
            time += str(self.__hour)
        if self.__minutes < 10:
            time += ":0" + str(self.__minutes)
        else:
            time += ":" + str(self.__minutes)
        if self.__seconds < 10:
            time += ":0" + str(self.__seconds)
        else:
            time += ":" + str(self.__seconds)

        return time

    def next_second(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hour == 23:
                    self.__hour = 0
                else:
                    self.__hour += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1

    def prev_second(self):
        if self.__seconds == 0:
            self.__seconds = 59
            if self.__minutes == 0:
                self.__minutes = 59
                if self.__hour == 0:
                    self.__hour = 23
                else:
                    self.__hour -= 1
            else:
                self.__minutes -= 1
        else:
            self.__seconds -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
