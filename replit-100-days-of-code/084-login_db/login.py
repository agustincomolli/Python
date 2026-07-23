from flask import Flask, request, redirect
from random import randint
import sqlite3
import os
import hashlib


def create_db():
    """
    Description: Crea la base de datos en caso de que no exista.
    """

    try:
        # Crear la base de datos.
        connection = sqlite3.connect("./data/users.db")
        # Crear el cursor.
        cursor = connection.cursor()
        # Crear la tabla usuarios.
        command_sql = "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password BLOB, salt INTEGER)"
        cursor.execute(command_sql)
        # Guardar los cambios.
        connection.commit()
        # Cerrar la conexión.
        connection.close()
    except:
        print("No se puede crear la base de datos.")


def is_valid(login: dict):
    """
    Description: Valida si los datos de inicio de sesión coinciden con la base de datos.
    Parameters:  - login: diccionario con los datos ingresados por el usuario.
    """

    # Verificar si existe la base de datos.
    if not os.path.exists("./data/users.db"):
        create_db()
        return False

    # Crear la conexión a la base de datos.
    connection = sqlite3.connect("./data/users.db")
    # Crear el cursor.
    cursor = connection.cursor()
    # Ejecutar la consulta buscando el usuario.
    command_sql = f"SELECT * FROM users WHERE name = '{login['user']}'"
    cursor.execute(command_sql)
    # Obtener los resultados de la consulta.
    results = cursor.fetchone()
    # Cerrar la conexión.
    connection.close()

    valid = False

    if results != None:
        salt = results[4]
        password = f"{login['password']}{salt}"
        hashed_password = hashlib.sha256(password.encode()).digest()
        if results[2] == login["email"] and results[3] == hashed_password:
            valid = True

    return valid


app = Flask(__name__, static_url_path="/static")


@app.route("/signup", methods=["POST"])
def signup():
    form = request.form
    # Fortalecer la contraseña.
    salt = randint(1000, 9999)
    password = f"{form['password']}{salt}"
    # Encriptar la contraseña.
    hashed_password = hashlib.sha256(password.encode()).digest()
    # Verificar si existe la base de datos.
    if not os.path.exists("./data/users.db"):
        create_db()
    # Crear la conexión a la base de datos.
    connection = sqlite3.connect("./data/users.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Insertar nuevo registro.
    command_sql = "INSERT INTO users (name, email, password, salt) VALUES (?, ?, ?, ?)"
    cursor.execute(command_sql,(form["user"], form["email"], hashed_password, salt))
    # Guardar los cambios.
    connection.commit()
    # Cerrar la conexión.
    connection.close()
    # Redirigir al usuario a la página principal.
    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    form = request.form

    with open("./templates/template.html", mode="r", encoding="UTF-8") as file:
        page = file.read()

    if is_valid(form):
        message = f"<h2 class='message'>Bienvenido {form['user']}</h2>"
        message += "<p class='icon'>😎</p>"
    else:
        message = f"<h2 class='message'>Los datos ingresados no son correctos</h2>"
        message += "<p class='icon'>😵‍💫</p>"

    page = page.replace("{content}", message)

    return page


@app.route("/")
def index():
    with open("./static/index.html", mode="r", encoding="UTF-8") as file:
        page = file.read()

    return page


app.run(host="0.0.0.0", port=81)
