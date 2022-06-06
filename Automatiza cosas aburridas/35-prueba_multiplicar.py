import pyinputplus as pyip
import random
import time

numero_preguntas = 10
respuestas_correctas = 0
for pregunta in range(numero_preguntas):
    # Elegir dos números aleatorios entre 1 y 10:
    numero1 = random.randint(1, 10)
    numero2 = random.randint(1, 10)
    # Preguntar al usuario:
    pregunta = f"{numero1} x {numero2} = "
    try:
        respuesta = pyip.inputStr(pregunta, 
                                  allowRegexes=[f'^{numero1 * numero2}$'], 
                                  blockRegexes=[(".*", "Respuesta inválida")],
                                  timeout=8, limit=3)
    except pyip.TimeoutException:
        print("¡Tiempo agotado!")
        break
    except pyip.RetryLimitException:
        print("¡Demasiados intentos fallidos!")
        break
    else:
        print("¡Correcto!")
        respuestas_correctas += 1

time.sleep(1)
print(f"¡Has acertado {respuestas_correctas} de {numero_preguntas} preguntas!")
print("¡Hasta pronto!")