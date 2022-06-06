import pyinputplus as pyip

while True:
    pregunta = "¿Quieres mantener ocupado a un idiota durante horas?\n"
    respuesta = pyip.inputYesNo(pregunta, yesVal="sí", noVal="no")
    if respuesta == "no":
        print("Gracias. ¡Que tengas un buen día.!")
        break