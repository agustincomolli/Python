import csv

with open ("contacts.csv") as archivo:
    # Leer el formato del archivo csv.
    archivo_csv = csv.reader(archivo)
    for registro in archivo_csv:
        # Desempaquetar la línea de registro en distintas variables.
        nombre, direccion, telefono, email = registro
        print("Nombre: {}, Teléfono: {}, Correo: {}".format(nombre, telefono, email))
