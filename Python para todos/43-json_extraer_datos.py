import urllib.error, urllib.parse, urllib.request
import json
import ssl

# Ignorar errores de certificados SSL.
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

url = input("Ingrese la dirección: ")
archivo = urllib.request.urlopen(url, context=contexto)
datos = archivo.read().decode()

datos_json = json.loads(datos)

total = 0
cantidad = 0
for item in datos_json["comments"]:
    cantidad += 1
    total += item["count"]

print(len(datos), "caracteres recuperados.")
print("Recuento:", cantidad)
print("Suma:", total)