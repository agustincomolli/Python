import json

# Crear un diccionario de persona.
dict_persona = {"Nombre" : "Agustín", "Apellido" : "Comolli"}
# Agregar una clave-valor adicional.
dict_persona["Ciudad"] = "Cañuelas"

# Crear una lista de lenguajes de programación.
lst_lenguajes = ["Visual Basic", "Python", "Clipper 5"]

# Agregar la lista al diccionario en la clave "Lenguajes"
dict_persona["Lenguajes"] = lst_lenguajes

# Crear un diccionario de staff.
# Asignar una persona al puesto de Administrador de programa.
dict_staff = {}
dict_staff["Administrador de programa"] = dict_persona
print(f"Diccionario: {dict_staff}")

# Convertir diccionario en objeto JSON.
json_staff = json.dumps(dict_staff)

# Imprimir objeto JSON.
print(f"Objeto JSON: {json_staff}")