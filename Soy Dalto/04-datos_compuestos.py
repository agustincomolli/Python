# Listas, los datos se pueden modificar:
print("LISTAS:")
fruits = ["banana", "manzana", "pera", "duraznos"]
print(f"Frutas: {fruits}")
califications = [10,8,7,10,9]
print(f"Calificaciones: {califications}")
mixed_list = ["Agustín", 46, "agustincomolli@gmail.com", True]
print(f"Datos de usuario: {mixed_list}")
print(f"Email: {mixed_list[2]}")
mixed_list[0] = "Agustín Comolli"
#          |-----> Indice (index)
print(f"Usuario modificado: {mixed_list[0]}")

# Tuplas, los datos no se pueden modificar:
print("\nTUPLAS:")
cars = ("Ford K", "Fiat Topolino", "Chevrolet Spark", "Toyota Etios")
print(f"Autos: {cars}")

# Conjuntos, no se pueden modificar ni acceder por indices a sus elementos,
# no se guardan elementos duplicados.
print("\nCONJUNTOS:")
names = {"Agustín", "Lorena", "Agustín", "Adrián", "Carlitos"}
print(f"Nombres: {names}")

# Diccionario.
print("\nDICCIONARIOS")
user = {"Nombre": "Agustín",
        "Edad" : 46,
        "Estatura" : 1.62,
        "Es hombre" : True}
#             |        |-----> Valor (value)
#             |--------------> Clave (key)
print(f"Datos de usuario: {user}")
user["Nombre"] = "Agustín Comolli"
print(f"Nombre completo: {user['Nombre']}")