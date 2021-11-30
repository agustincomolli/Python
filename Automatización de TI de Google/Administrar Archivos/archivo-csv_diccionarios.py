import csv

usuarios = [{"nombre": "Sol Mansi", "usuario":"solm","area":"Infraestructura TI"},
{"nombre":"Lio Nelson","usuario":"lion", "area":"Investigación de experiencias de usuario"},
{"nombre":"Charlie Grey", "usuario":"greyc", "area":"Desarrollo"}]

claves = ["nombre","usuario","area"]

with open("usuarios.csv", "w") as archivo:
    archivo_csv = csv.DictWriter(archivo,fieldnames=claves)
    archivo_csv.writeheader()
    archivo_csv.writerows(usuarios)
