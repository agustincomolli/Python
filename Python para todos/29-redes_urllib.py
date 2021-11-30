# Recuperar los datos de romeo.txty calcular la frecuencia de cada 
# palabra en el archivo.
import urllib.request

archivo = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

lista_palabras = {}

for linea in archivo:
    palabras = linea.decode().split()
    for palabra in palabras:
        lista_palabras[palabra] = lista_palabras.get(palabra, 0) + 1

print(lista_palabras)