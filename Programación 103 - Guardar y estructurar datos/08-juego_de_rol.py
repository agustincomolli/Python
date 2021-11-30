import json
import os

def mostrar_instrucciones():
    # Imprime un menú principal y los comandos.
    mensaje = "Juego de rol \n"
    mensaje += "=============\n\n"
    mensaje += "Ve al jardín con un llave y una poción.\n"
    mensaje += "¡Evita a los monstruos!\n\n"
    mensaje += "Te estás cansando, cada vez que te mueves pierdes un punto de vida.\n\n"
    mensaje += "Comandos:\n"
    mensaje += "    ir [norte | sur | este | oeste]\n"
    mensaje += "    obtener [objeto]\n"
    print(mensaje)

def mostrar_estado():
    # Imprime el estado actual del jugador.
    print("---------------------------")
    print(f"{nombre} está en {habitacion_actual}.")
    print(f"Salud: {str(salud)}")
    # Imprimir el inventario actual.
    print(f"Inventario: {inventario}")
    # Imprimir un item si lo hay.
    if "item" in habitaciones[habitacion_actual]:
        print("Ves", habitaciones[habitacion_actual]["item"])
    print("---------------------------")

# Eliminar cualquier item de las habitaciones que ya esté en el inventario
# del jugador.
def eliminar_items():
    for habitacion in habitaciones.keys():
        # Si hay un item en la habitación...
        if "item" in habitaciones[habitacion]:
            # Si el item está en el inventario...
            if habitaciones[habitacion]["item"] in inventario:
                # Borrar el item de la habitación.
                del habitaciones[habitacion]["item"]

# - # CÓDIGO SE AÑADIRÁ AQUÍ EN EL SIGUIENTE PASO # - #
# Cargar datos del archivo.
try:
    print("Recuperando detalles del jugador...")
    with open("datos_del_juego.json", mode="r") as archivo:
        datos_juego = json.load(archivo)
        nombre = datos_juego["nombre_jugador"]
        salud = datos_juego["salud_jugador"]
        habitacion_actual = datos_juego["habitacion_actual_jugador"]
        inventario = datos_juego["inventario_jugador"]
except FileNotFoundError:
    print("No se encontró ningún juego anterior. Comenzando un nuevo juego...")
    # Configurar un nuevo juego.
    nombre = None
    salud = 5
    habitacion_actual = "Salón"
    inventario = []

# Comprobar la integridad de los datos cargados.
if (salud < 0) or (salud > 5):
    os.remove("datos_del_juego.json")
    print("\n¡Has hecho trampa! Los datos del juego han sido borrados.\n")
    # Configurar un nuevo juego.
    nombre = None
    salud = 5
    habitacion_actual = "Salón"
    inventario = []

# Crear un diccionario que une una habitación a otras posiciones de la habitación.
habitaciones = {
    "Salón" : {"sur" : "Cocina",
            "este" : "Comedor",
            "item" : "llave"
            },
    "Cocina" : {"norte" : "Salón",
                "item" : "monstruo"
                },
    "Comedor" : {"oeste" : "Salón",
                "sur" : "Jardín",
                "item" : "poción"
                },
    "Jardín" : {"norte" : "Comedor"}
}

eliminar_items()

# Preguntar el nombre al jugador.
if nombre is None:
     nombre = input ("¿Cuál es tu nombre, aventurero? ")
     mostrar_instrucciones()

# Generar un bucle sin fin.
while True:
    mostrar_estado()
    
    # Obtener el siguiente "movimiento" del jugador
    # .split () lo divide en una matriz de lista
    # p.ej. escribir "ir al este" daría la lista:
    # ["ir", "este"]
    mover = ""
    while mover == "":
        mover = input("> ")

    mover = mover.lower().split()

    # Si escribe "ir" en primer lugar...
    if mover[0] == "ir":
        salud -= 1
        # Comprobar que se le permita ir donde quiera...
        if mover[1] in habitaciones[habitacion_actual]:
            # Establecer la habitación actual con la nueva ubicación.
            habitacion_actual = habitaciones[habitacion_actual][mover[1]]
        # Si no hay puerta en esa dirección.
        else:
            print("¡No puedes ir por ahí!")

    # Si escribe "obtener" en primer lugar...
    if mover[0] == "obtener":
        # Si la habitación contiene un item, y es el que el usuario
        # quiere obtener...
        if "item" in habitaciones[habitacion_actual] and \
        mover[1] in habitaciones[habitacion_actual]["item"]:
            # Agregar el item a su inventario.
            inventario += [mover[1]]
            # Mostrar un mensaje de información.
            print(f"¡{mover[1]} obtenido!")
            # Borrar el item de la habitación.
            del habitaciones[habitacion_actual]["item"]
        # De lo contrario, si el item no está en esa habitación...
        else:
            # Informar que el item no está ahí.
            print(f"El item {mover[1]} que quieres obtener no está aquí.")
        
    # Si hay un monstruo en la habitación... el jugador pierde la partida.
    if "item" in habitaciones[habitacion_actual] and \
    "monstruo" in habitaciones[habitacion_actual]["item"]:
        print("Un monstruo te ha atrapado.\n\n¡JUEGO TERMINADO!")
        break

    if salud == 0:
        print("Te derrumbas por cansancio.\n\n¡JUEGO TERMINADO!")
        break

    # Si el jugador llega al jardín con una llave y una poción... GANA.
    if habitacion_actual == "Jardín" and "llave" in inventario and \
    "poción" in inventario:
        print("Has logrado escapar de la casa.\n\n¡FELICITACIONES GANASTE EL JUEGO!")
        break

    # - # CÓDIGO SE AÑADIRÁ AQUÍ EN EL SIGUIENTE PASO # - #
    # Guarde los datos del juego en el archivo
    datos_juego = {
        "nombre_jugador" : nombre,
        "salud_jugador" : salud,
        "habitacion_actual_jugador" : habitacion_actual,
        "inventario_jugador" : inventario
    }

    with open("datos_del_juego.json", mode="w") as archivo:
        json.dump(datos_juego, archivo)