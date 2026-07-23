import urllib.error, urllib.parse, urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignorar errores de certificados SSL
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

# url = "http://py4e-data.dr-chuck.net/comments_42.html"
url = "http://py4e-data.dr-chuck.net/comments_1366235.html"
html = urllib.request.urlopen(url, context=contexto).read()
sopa = BeautifulSoup(html, "html.parser")

etiquetas = sopa("span")
total = 0
for etiqueta in etiquetas:
    total += int(etiqueta.contents[0])

print(total)