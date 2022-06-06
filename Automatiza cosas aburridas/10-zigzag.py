import time, sys

sangria = 0 # Cuántos espacios sangrar.
aumenta_sangria = True # Si la sangría aumenta o no.

try:
    while True:
        print(" " * sangria, end="")
        print("********")
        time.sleep(0.1) # Pausar 1/10 segundo.

        if aumenta_sangria:
            # Aumentar el número de espacios.
            sangria += 1

            if sangria == 20:
                # Cambiar la dirección.
                aumenta_sangria = False
        else:
            sangria -= 1
            if sangria == 0:
                # Cambiar dirección.
                aumenta_sangria = True
except KeyboardInterrupt:
    print("\n¡Hasta la próxima!")
    sys.exit()