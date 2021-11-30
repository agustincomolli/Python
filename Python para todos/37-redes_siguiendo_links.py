import urllib.error, urllib.parse, urllib. request
import ssl
from bs4 import BeautifulSoup

# Ignorar errores de certificados SSL.
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

url = input("Ingrese la URL: ")
try:
    recuento = int(input("Ingrese recuento: "))
    posicion = int(input("Ingrese posición: "))
except:
    print("ERROR: Debe ingresar un número.")
    quit()

for i in range(recuento):
    html = urllib.request.urlopen(url, context=contexto).read()
    sopa = BeautifulSoup(html, "html.parser")

    etiquetas = sopa("a")
    print(etiquetas[posicion -1].get("href"))
    url = etiquetas[posicion -1].get("href")

print(etiquetas[posicion - 1].contents[0])