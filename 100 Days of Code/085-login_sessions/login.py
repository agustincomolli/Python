from flask import Flask, request, redirect, session
from random import randint  # Para fortalecer la contraseña.
import sqlite3  # Para manejar la base de datos.
import os
import hashlib  # Para encriptar la contraseña.
import secrets  # Para generar clave secreta en las sesiones.


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
    command_sql = f"SELECT * FROM users WHERE email = '{login['email']}'"
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
        if results[3] == hashed_password:
            valid = True
            # Guardar el nombre de usuario en la sesión.
            session["user"] = results[1]

    return valid


def generate_secret_key():
    # Generar una clave secreta de 32 bits para ser usada en la sesión del usuario.
    secret_key = secrets.token_hex(32)
    # os.environ.setdefault("SECRET_KEY", secret_key)
    return secret_key


app = Flask(__name__, static_url_path="/static")
app.secret_key = generate_secret_key()


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


@app.route("/alredy")
def alredy():
    with open("./templates/template.html", mode="r", encoding="UTF-8") as file:
        page = file.read()

    user = session.get("user")
    title = f"{user}"
    message = f"<h2 class='message'>Ya iniciaste sesión, no jodás más.</h2>"
    message += "<p class='icon'>🤌</p>"
    url = "'/reset'"
    message += f"<p class='session'><button type='button' onclic='location.href={url}'>"
    message += "Cerrar sesión</button></p>"

    page = page.replace("{title}", title)
    page = page.replace("{content}", message)

    return page


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
    cursor.execute(
        command_sql, (form["user"], form["email"], hashed_password, salt))
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
        user = session.get("user")
        title = "Has iniciado sesión correctamente 🔓"
        message = f"<h2 class='message'>Bienvenido {user}</h2>"
        message += "<p class='icon'>😎</p>"
    else:
        title = "No has iniciado sesión 🔒"
        message = f"<h2 class='message'>Los datos ingresados no son correctos</h2>"
        message += "<p class='icon'>😵‍💫</p>"

    page = page.replace("{title}", title)
    page = page.replace("{content}", message)

    return page


@app.route("/")
def index():
    if session.get("user"):
        return redirect("/alredy")

    with open("./static/index.html", mode="r", encoding="UTF-8") as file:
        page = file.read()

    return page


app.run(host="0.0.0.0", port=81)
