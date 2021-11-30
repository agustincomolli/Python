import urllib.request

pagina_web = input("Ingrese la URL: ")
total_recibido = 0

archivo = urllib.request.urlopen(pagina_web)

for linea in archivo:
    total_recibido += len(linea.decode())
    if total_recibido <= 3000:
        print(linea.decode().strip())

print("\nTotal de caracteres recibidos:", total_recibido)
