import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, request, redirect


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


def get_tracks(artist: str):
    client_id = get_client_id()
    client_secret = get_client_secret()
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.post(url, data=data, auth=auth)
    access_token = response.json()["access_token"]

    endpoint_url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {access_token}"}
    search = f"?q=artist%3D{artist}&type=track&market=ES&limit=10"
    full_url = f"{endpoint_url}{search}"

    response = requests.get(full_url, headers=headers)
    data = response.json()

    return data["tracks"]["items"]
