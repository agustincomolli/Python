import urllib.error, urllib.parse, urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignorar errores de certificados SSL.
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

# Ingresar una url para buscar todos los párrafos.
url = input("Ingrese una url: ")
html = urllib.request.urlopen(url, context=contexto).read()
sopa = BeautifulSoup(html, "html.parser")

# Contar todos los párrafos de la página.
etiquetas = sopa("p")
cant_parrafos = 0
for etiqueta in etiquetas:
    cant_parrafos += 1

print(f"Hay {cant_parrafos} de párrafos en el documento.")
