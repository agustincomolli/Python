# Calcular puntaje.
def obtener_calificacion(puntaje):
    calificacion = ""
    if puntaje < 1:
        if puntaje >= 0.9:
            calificacion = "A"
        elif puntaje >= 0.8:
            calificacion = "B"
        elif puntaje >= 0.7:
            calificacion = "C"
        elif puntaje >= 0.6:
            calificacion = "D"
        else:
            calificacion = "F"
    else:
        calificacion = ""
    return calificacion


print("Calculador de puntajes\n" + "=" * 22)
try:
    puntaje = float(input("\nPuntaje: "))
except:
    print("ERROR: Debe ingresar un valor numérico")
    quit()

calificacion = obtener_calificacion(puntaje)
if calificacion != "":
    print("Su calificación es '" + calificacion + "'\n")
else:
    print("Debe ingresar un número entre 0 y 1")
