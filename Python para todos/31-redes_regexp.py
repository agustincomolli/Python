# Buscar valores de enlace dentro de la entrada de URL
import urllib.error, urllib.parse, urllib.request
import re
import ssl

# Ignorar los errores de certificado SSL.
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

url = input("Ingrese la url: ")
html = urllib.request.urlopen(url, context=contexto).read()
vinculos = re.findall(b'href=("http[s]?://.*?")', html)
for vinculo in vinculos:
    print(vinculo.decode())