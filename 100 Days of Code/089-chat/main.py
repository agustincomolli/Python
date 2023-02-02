from flask import Flask, request, redirect, session
from datetime import datetime
import os
import sqlite3
import secrets


def is_valid_user(user_login: dict):
    """
    Description: Valida si los datos de inicio de sesión coinciden con la base de datos.
    Parameters:  - login: diccionario con los datos ingresados por el usuario.
    """

    # Crear la conexión con la base de datos.
    connection = sqlite3.connect("./data/chat.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Ejecutar la consulta buscando el usuario.
    command_sql = f"SELECT * FROM users WHERE username = '{user_login['user']}'"
    cursor.execute(command_sql)
    # Obtener el resultado de la consulta.
    result = cursor.fetchone()
    # Cerrar la conexión a la base de datos.
    connection.close()

    valid = False

    if result != None and result[2] == user_login["password"]:
        valid = True
        session["id"] = result[0]
        session["name"] = result[1]
        session["emoji"] = result[3]

    return valid


def open_page(file_name: str):
    """
    Description: Abre un archivo html y devuelve su contenido.
    Parameter:   - file_name: nombre del archivo a abrir.
    """

    with open(file_name, mode="r", encoding="UTF-8") as file:
        page = file.read()

    return page


def get_emoji():
    """
    Description: Devuelve una lista de emojis para seleccionar como avatar.
    """

    faces = [
        "😀", "😁", "😉", "😎", "🥰", "😍", "🤗", "🤪",
        "🤔", "😑", "😶", "😶‍🌫️", "🙄", "😮", "🤐", "😫",
        "🥱", "😴", "😓", "🙃", "🤑", "😖", "😟", "😤",
        "🥸", "🤠", "🤡", "🤥", "🤓", "😈", "👺", "💀",
        "😵‍💫", "😡", "🤯", "🥶", "🥵", "😇", "🥳", "😱",
    ]

    return faces


def get_chat_data():
    """
    Description: obtiene todos los mensajes de chat.
    """

    # Crear la conexión a la base de datos.
    connection = sqlite3.connect("./data/chat.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Ejecutar la consulta a la base de datos.
    command_sql = "SELECT users.username, users.emoji, chats.*"
    command_sql += "FROM users INNER JOIN chats ON users.id = chats.user_id"
    cursor.execute(command_sql)
    results = cursor.fetchall()
    # Cerrar la conexión a la base de datos.
    connection.close()

    return results


def add_chat_db(date: datetime, user_id: int, chat: str):
    """
    Description: Agrega una entrada al chat.
    """

    # Crear la conexión a la base de datos.
    connection = sqlite3.connect("./data/chat.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Ejecutar la instrucción SQL.
    command_sql = "INSERT INTO chats (date, user_id, chat) VALUES (?, ?, ?)"
    cursor.execute(command_sql, (date, user_id, chat,))
    # Guardar los cambios.
    connection.commit()
    # Cerrar la base de datos.
    connection.close()


def add_user_db(username: str, password: str, emoji: str, role: str):
    """
    Description: Agrega un nuevo usario a la base de datos.
    """

    # Crear la conexión a la base de datos.
    connection = sqlite3.connect("./data/chat.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Insertar el nuevo usuario.
    command_sql = "INSERT INTO users (username, password, emoji, role) "
    command_sql += "VALUES (?, ?, ?, ?)"
    cursor.execute(command_sql, (username, password, emoji, role,))
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

    # Insertar el usuario administrador.
    command_sql = "INSERT INTO users (username, password, emoji, role) "
    command_sql += "VALUES (?, ?, ?, ?)"
    cursor.execute(command_sql, ("agustincomolli", "admin", "🤪", "admin"))

    # Crear la tabla chats.
    command_sql = "CREATE TABLE chats (id INTEGER PRIMARY KEY, date DATETIME, "
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


if not os.path.exists("./data/chat.db"):
    create_db()

app = Flask(__name__, static_url_path="/static")
app.secret_key = generate_secret_key()


@app.route("/send", methods=["POST"])
def send():
    form = request.form

    if form["message"] != "":
        add_chat_db(datetime.now(), session["id"], form["message"])
        return redirect("/")


@app.route("/chat")
def chat():
    if not session.get("id"):
        return redirect("/")

    chat_data = get_chat_data()
    chat =""

    for record in chat_data:
        date_message = datetime.strptime(record[3], "%Y-%m-%d %H:%M:%S.%f")
        date_message = datetime.strftime(date_message, "%d/%m/%Y a las %H:%M")
        message = "<div class='container-message'>"
        message += f"<p class='user-message'>{record[1]} " 
        message += f"<span class='username'>{record[0]}</span> dice: </p>"
        message += f"<p class='date-message'>{date_message}</p>"
        message += f"<p class='chat-message'>{record[5]}</p>"
        message += "</div>"
        chat += message

    page = open_page("./static/chat.html")
    page = page.replace("{h1}", f"Chateame - {session['emoji']}")
    page = page.replace("{content}", chat)

    return page


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    form = request.form

    if not is_valid_user(form):
        page = open_page("./static/login.html")
        html_code = "</form><h2 class='message'>Los datos ingresados no son correctos</h2>"
        html_code += "<p class='icon'>😵‍💫</p>"
        page = page.replace("</form>", html_code)

        return page
    else:
        return redirect("/chat")


@app.route("/login-form")
def login_form():
    if session.get("id"):
        return redirect("/chat")
        
    return open_page("./static/login.html")


@app.route("/signup", methods=["POST"])
def signup():
    form = request.form

    add_user_db(form["user"], form["password"], form["emoji"], "user")

    return redirect("/")


@app.route("/register")
def register():
    if session.get("id"):
        return redirect("/chat")
        
    page = open_page("./static/signup.html")
    html_code = ""

    for emoji in get_emoji():
        html_code += f"<option>{emoji}</option>"

    page = page.replace("{emojis}", html_code)

    return page


@app.route("/")
def index():
    if session.get("id"):
        return redirect("/chat")

    return open_page("./static/index.html")


app.run(host="0.0.0.0", port=81)
