import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificados SSL.
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

# Ingresar una url para buscar todos los vínculos.
url = input("Ingrese una url: ")
html = urllib.request.urlopen(url, context=contexto).read()
sopa = BeautifulSoup(html, "html.parser")

# Mostrar todos los hipervínculos de la página.
etiquetas = sopa("a")
for etiqueta in etiquetas:
    print(etiqueta.get("href", None))
