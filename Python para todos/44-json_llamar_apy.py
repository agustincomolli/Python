import urllib.error, urllib.parse, urllib.request
import json
import ssl

api_key = False
# Si tiene una clave API de Google Places, ingrésela aquí
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if not api_key: #is False:
    api_key = 42
    servicio_url = "http://py4e-data.dr-chuck.net/json?"
else:
    servicio_url = "https://maps.googleapis.com/maps/api/geocode/json?"

# Ignorar errores de certificados SSL.
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

direccion = input("Ingrese la dirección: ")

parametros = {}
parametros["address"] = direccion
if api_key: parametros["key"] = api_key
url = servicio_url + urllib.parse.urlencode(parametros)

print("Recuperando:", url, "caracteres...")
archivo = urllib.request.urlopen(url, context=contexto)
datos = archivo.read().decode()

try:
    datos_json = json.loads(datos)
except:
    datos_json = None

if (not datos_json) or ("status" not in datos_json) \
or (datos_json["status"] != "OK"):
    print("==== Falla al recuperar ====")
    print(datos)
    quit()

pid = datos_json["results"][0]["place_id"]
print("ID:", pid)
