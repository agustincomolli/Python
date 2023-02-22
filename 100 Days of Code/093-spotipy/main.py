import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, request, redirect
from datetime import datetime


def get_client_id():
    """
    Description: Devuelve el Client ID de Spotify
    """

    with open("./093-spotipy_secrets.dat", "r", encoding="UTF-8") as file:
        return file.readline().strip()


def get_client_secret():
    """
    Description: Devuelve el Client Secret de Spotify
    """

    with open("./093-spotipy_secrets.dat", "r", encoding="UTF-8") as file:
        file.readline()
        return file.readline().strip()


def get_tracks(year: str):
    """
    Description: Realiza una búsqueda en la base de datos de Spotify según
                 el año.
    Parameters:  - year: Año a buscar.
    Return:      Devuelve un diccionario con las 10 canciones según el año.
    """

    client_id = get_client_id()
    client_secret = get_client_secret()
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.post(url, data=data, auth=auth)
    access_token = response.json()["access_token"]

    endpoint_url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {access_token}"}
    search = f"?q=year%3A{year}&type=track&market=ES&limit=10"
    full_url = f"{endpoint_url}{search}"

    response = requests.get(full_url, headers=headers)
    data = response.json()

    return data["tracks"]["items"]


def open_page(file_name: str):
    """
    Description: Abre un archivo html y devuelve su contenido.
    Parameter:   - file_name: nombre del archivo a abrir.
    """

    with open(file_name, mode="r", encoding="UTF-8") as file:
        page = file.read()

    return page


def generate_html_tracks(tracks: dict):
    html = "<div class='track-list'>"

    for track in tracks:
        track_name = track["name"]
        artist = track["album"]["artists"][0]["name"]
        url = track["preview_url"]
        html += f"<h4>{track_name} por {artist}</h4>"
        html += "<audio controls>"
        html += f"<source src='{url}' type='audio/mpeg'>"
        html += "</audio>"
        html += "<hr>"

    html += "</div>"
    return html


app = Flask(__name__, static_url_path="/static")


@app.route("/search", methods=["POST"])
def search():
    form = request.form
    year = form["year"]
    tracks_dict = get_tracks(year)
    html_code = generate_html_tracks(tracks_dict)

    print(html_code)

    page = open_page("./static/index.html")
    year = str(datetime.now().year)
    page = page.replace("{year}", year)
    page = page.replace("<div name=\"track-list\"></div>", html_code)

    return page


@app.route("/")
def index():
    page = open_page("./static/index.html")
    actual_year = str(datetime.now().year)
    page = page.replace("{year}", actual_year)

    return page


app.run(host="0.0.0.0", port=81)
