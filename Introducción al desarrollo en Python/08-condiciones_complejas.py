# Un estudiante tiene grado de honor si su promedio es >= 0.85
# y si su calificación más baja es de 0.70.

promedio_calificaciones = 0
calificacion_mas_baja = 0
grado_de_honor = False

try:
    promedio_calificaciones = float(\
        input("Ingrese el promedio de calificaciones: "))
    calificacion_mas_baja = float( \
        input("Ingrese la calificación más baja: "))
except:
    print("ERROR: Debe ingresar un número.")
    quit()

if promedio_calificaciones >= 0.85 and calificacion_mas_baja >= 0.70:
    grado_de_honor = True

if grado_de_honor:
    print("¡Felicidades estás en la lista de honor!")