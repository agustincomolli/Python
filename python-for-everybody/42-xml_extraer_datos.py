import urllib.error, urllib.parse, urllib.request
import xml.etree.ElementTree as ElementTree
import ssl

# Ignorar errores de certificados SSL
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

url = input("Ingrese la dirección: ")

print("Recuperando: ", url)
archivo = urllib.request.urlopen(url, context=contexto)
datos = archivo.read()
arbol = ElementTree.fromstring(datos)
lista_datos = arbol.findall(".//count")
total = 0
cantidad = 0
for elemento in lista_datos:
    cantidad += 1
    total += int(elemento.text)

print(len(datos), "caracteres recuperados.")
print("Recuento:", cantidad)
print("Suma:", total)