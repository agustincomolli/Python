from flask import Flask, request, redirect, session
from datetime import datetime
import os
import sqlite3
import secrets


def get_emoji():
    """
    Description: Devuelve una lista de emojis para seleccionar como avatar.
    """

    faces = [
        "😀", "😁", "😉", "😎" , "🥰", "😍", "🤗", "🤪"
        "🤔", "😑", "😶", "😶‍🌫️" , "🙄", "😮", "🤐", "😫"
        "🥱", "😴", "😓", "🙃" , "🤑", "😖", "😟", "😤"
        "🥸", "🤠", "🤡", "🤥" , "🤓", "😈", "👺", "💀"
        "😵‍💫", "😡", "🤯", "🥶", "🥵", "😇", "🥳", "😱"
    ]

    return faces

def add_user_db(username:str, password:str, emoji:str, role:str):
    """
    Description: Agrega un nuevo usario a la base de datos.
    """

    # Crear la conexión a la base de datos.
    connection = sqlite3.connect("./data/chat.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Insertar el nuevo usuario.
    command_sql = ""
    cursor.execute(command_sql)
    # Guardar los cambios.
    connection.commit()
    # Cerrar la conexión a la base de datos.
    connection.close()


def create_db():
    """
    Description: Crear la base de datos
    """
    
    # Crear la conexión a la base de datos.
    connection = sqlite3.connect("./data/chat.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()

    # Crear la tabla usuarios.
    command_sql = "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, " 
    command_sql += "password TEXT, emoji TEXT, role TEXT)"
    cursor.execute(command_sql)

    # Crear la tabla chats.
    command_sql = "CREATE TABLE chats (id INTEGER PRIMARY KEY, date DATETIME "
    command_sql += "user_id INTEGER, chat TEXT)"
    cursor.execute(command_sql)

    # Guardar los cambios.
    connection.commit()
    # Cerrar la conexión a la base de datos.
    connection.close()


def generate_secret_key():
    """
    Description: Generar una clave secreta de 32 bits para ser usada en la 
                 sesión del usuario.
    """

    return secrets.token_hex(32)


app = Flask(__name__, static_url_path="/static")
app.secret_key = generate_secret_key()


app.run(host="0.0.0.0", port=81)
