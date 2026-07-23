import json

datos = '''
[
    {
        "id" : "001",
        "x" : "2",
        "nombre" : "Agustín"
    },
    {
        "id" : "002",
        "x" : "7",
        "nombre" : "Lorena"
    }
]
'''
usuarios = json.loads(datos)
print("Cantidad de usuarios:", len(usuarios), "\n")

for usuario in usuarios:
    print("Nombre:", usuario["nombre"])
    print("ID:", usuario["id"])
    print("Atributo:", usuario["x"], "\n")