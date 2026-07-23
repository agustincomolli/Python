from datetime import datetime

def es_dia_semana(fecha):
    # Obtener el número del día de la semana: lunes = 0, martes = 1, etc.
    dia = fecha.weekday()

    if dia < 5:
        return True
    else:
        return False

if es_dia_semana(datetime.now()):
    print("Es día de semana... ¡A trabajar!")
else:
    print("¡Es fin de semana! ¡Joda")

