"""
Organizando datos con claves-valor de los diccionarios.
"""

birthdays = {
    "Agustín": "10 de junio",
    "Lorena": "18 de octubre",
    "Carlitos": "6 de octubre",
    "Adrián": "30 de julio"
}

while True:
    print("Ingrese un nombre (dejar en blanco para salir)")
    name = input("> ")

    if name == "":
        break

    if name in birthdays:
        print("El " + birthdays[name] + " es el cumpleaños de " + name)
    else:
        print("No tengo información del cumpleaños de " + name)
        print("¿Cuándo es su cumpleaños?")
        birthday_date = input("> ")
        birthdays[name] = birthday_date
        print("Base de datos de cumpleaños actualizada.")
