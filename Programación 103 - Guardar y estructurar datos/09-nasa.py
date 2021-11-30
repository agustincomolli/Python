import requests
import webbrowser

# Abrir datos de url.
apod_api_solicitud = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
# Convertir datos a formato json y crear un diccionario.
apod = apod_api_solicitud.json()
# Extraer del diccionario la url de la imagen.
imagen_url = apod["url"]
# Abrir la imagen en el navegador predeterminado.
webbrowser.open(imagen_url)