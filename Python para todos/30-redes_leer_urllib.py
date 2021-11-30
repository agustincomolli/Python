import urllib.request, urllib.parse, urllib.error

imagen = urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")

archivo = open("cubierta3.jpg", mode="wb")
tamaño = 0

while True:
    informacion = imagen.read(100000)
    if len(informacion) < 1: break
    tamaño += len(informacion)
    archivo.write(informacion)

print(f"Se han copiado {tamaño} caracteres.")
archivo.close()