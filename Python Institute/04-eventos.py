# Escenario:

# La tarea es preparar un código simple para evaluar o encontrar el tiempo 
# final de un periodo de tiempo dado, expresándolo en horas y minutos. Las 
# horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado 
# en la consola.

# Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará 
# a las 13:16.

hour = int(input("Hora de inicio (horas): "))
minutes = int(input("Minuto de inicio (minutos): "))
duration = int(input("Duración del evento (minutos): "))

# Se convierte la hora de inicio en minutos y se le suma los minutos de la 
# hora de inicio.
total_minutes = hour * 60
total_minutes += minutes
# Se le suma la duración del evento a los minutos totales.
total_minutes += duration

# Se convierten los minutos totales a horas y se calcula la hora final del 
# evento.
total_hours = (total_minutes // 60)
# Obtener el resto de la división de las horas totales por 24 para que no
# excedan las 24 horas del día
final_hour = (total_hours // 60) % 24

# Se calculan los minutos finales del evento.
final_minutes = total_minutes % 60
print(f"El evento finalizará a las {final_hour}:{final_minutes}")
