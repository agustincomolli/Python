cumpleaños = {
    "agustín":"10 de junio",
    "carlitos":"6 de octubre", 
    "adrián":"31 de julio", 
    "lorena":"18 de otubre",
    "gustavo":"24 de nviembre"
    }

while True:
    nombre = input("Ingrese un nombre (en blanco para salir): ").lower()
    if nombre == "":
        break

    if nombre in cumpleaños:
        print(f"El cumpleaños de {nombre.capitalize()} es el {cumpleaños[nombre]}.")
    else:
        print(f"No tengo información de cumpleaños para {nombre}.")
        nuevo_cumpleaños = input("¿Cuándo es su cumpleaños? ")
        # Agregar nuevo valor al diccionario.
        cumpleaños[nombre] = nuevo_cumpleaños
        print("¡Base de datos actualizada!")

# Recorrer todo el diccionario y listar su contenido.
for nombre, fecha in cumpleaños.items():
    print(f"{nombre.capitalize()} cumple el {fecha}.")