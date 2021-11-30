# Muestra un mensaje en la pantalla.
def mostrar(mensaje, es_alerta=False):
    if es_alerta:
        print("¡Alerta!",)
    print(mensaje)