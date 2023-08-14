# Crear una excepción personalizada.
class MyException(Exception):
    def __init__(self, err):
        print(f"ERROR: {err}")


try:
    # Lanza una excepción.
    raise MyException("¡Qué cagada loco!")
except:
    print("😧")