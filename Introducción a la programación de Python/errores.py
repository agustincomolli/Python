while True:
    try:
        numero = int(input("Ingrese un número: "))
    except ValueError: # Detecta solo errores de valor.
        print("¡No es un número entero! Intente nuevamente.")
    except KeyboardInterrupt:
        print("\n", "*** ¡Noooo, interrumpiste el programa! ***".center(80, " "))
        break
    else:
        print("¡Muy bien!")
        break # Sin esta instrucción no saldría del bucle.
    finally:
        print("Intento de entrada")