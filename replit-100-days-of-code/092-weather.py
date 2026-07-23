import requests
from mylib import *

# Diccionario para los códigos climáticos y sus respectivos emojis
weather_codes = {
    0: "Cielo despejado ☀️",
    1: "Mayormente despejado 🌤️",
    2: "Parcialmente nublado 🌤️",
    3: "Nublado 🌤️",
    45: "Niebla 🌫️",
    48: "Niebla con raspón 🌫️",
    51: "Llovizna de intensidad ligera 🌧️",
    53: "Llovizna de intensidad moderada 🌧️",
    55: "Llovizna de intensidad densa 🌧️",
    56: "Llovizna congelada de intensidad ligera ❄️🌧️",
    57: "Llovizna congelada de intensidad densa ❄️🌧️",
    61: "Lluvia de intensidad ligera 🌧️",
    63: "Lluvia de intensidad moderada 🌧️",
    65: "Lluvia de intensidad fuerte 🌧️",
    66: "Lluvia congelada de intensidad ligera ❄️🌧️",
    67: "Lluvia congelada de intensidad fuerte ❄️🌧️",
    71: "Nevada de intensidad ligera 🌨️",
    73: "Nevada de intensidad moderada 🌨️",
    75: "Nevada de intensidad fuerte 🌨️",
    77: "Copos de nieve ❄️",
    80: "Chubascos de lluvia de intensidad ligera 🌦️",
    81: "Chubascos de lluvia de intensidad moderada 🌦️",
    82: "Chubascos de lluvia de intensidad fuerte 🌦️",
    85: "Chubascos de nieve de intensidad ligera ❄️🌦️",
    86: "Chubascos de nieve de intensidad fuerte ❄️🌦️",
    95: "Tormenta eléctrica de intensidad moderada ⚡️",
    96: "Tormenta eléctrica con granizo ligero ⚡️💧",
    99: "Tormenta eléctrica con granizo fuerte ⚡️💧"
}

# Zona horaria de Argentina
timezone = "ART" 

# Coordenadas de Cañuelas
latitude = -35.059601
longitude = -58.750660

# Hacer una petición a la API de Open-Meteo para obtener información del clima
result = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&" +
    f"longitude={longitude}&daily=weathercode,temperature_2m_max," +
    f"temperature_2m_min&timezone={timezone.upper()}")

# Transfomar el resultado de la API en formato JSON
user = result.json()
# Obtener los valores de clima...
today_weather_code = user["daily"]["weathercode"][0]
# ... temperatura máxima del día actual.
today_max_temp = user["daily"]["temperature_2m_max"][0]
# ... temparatura mínima del día actual.
today_min_temp = user["daily"]["temperature_2m_min"][0]

# Mostrar los datos en pantalla.
clear_screen()
print(color_me("*** El clima para hoy ***\n", "yellow"))
print(weather_codes[today_weather_code])
print("\nLa temperatura para hoy será:")
print(f"🥵: {today_max_temp}° y 🥶: {today_min_temp}°\n")