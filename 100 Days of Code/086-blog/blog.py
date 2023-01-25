from flask import Flask, request, redirect, session
from datetime import datetime
import sqlite3
import os
import secrets  # Para generar la clave secreta para las sesiones.


def is_valid_user(user_login:dict):
    """
    Description: Valida si los datos de inicio de sesión coinciden con la base de datos.
    Parameters:  - login: diccionario con los datos ingresados por el usuario.
    """

    # Crear la conexión con la base de datos.
    connection = sqlite3.connect("./data/blog.db")
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

    if result != None and result[3] == user_login["password"]:
        valid = True
        session["login"] = True
        session["name"] = result[2]

    return valid


def create_blog_page():
    """
    Description: Crea el código HTML con los datos del blog.
    """

    data_blog = get_data_blog()
    blog = ""

    for record in data_blog:
        entry = f"<h2>{record[2]}</h2>"
        blogdate = datetime.strptime(record[1], "%Y-%m-%d").date()
        entry += f"<p class='date'>{blogdate.strftime('%d-%m-%Y')}</p>"
        entry += f"<p>{record[3]}</p><hr>"
        blog += entry

    return blog


def create_simple_form():
    """
    Description: Crea código HTML con un formulario que tiene solamente
                 un botón de inicio de sesión.
    """

    html_code = "<form action='/login-form'>"
    html_code += "<input type='submit' value='Iniciar sesión'>"
    html_code += "</form>"

    return html_code


def insert_blog_entry(date: datetime, title: str, content: str):
    # Crear la conexión a la base de datos.
    connection = sqlite3.Connection("./data/blog.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Agregar la entrada al blog.
    command_sql = "INSERT INTO blog (date, title, content) VALUES (?, ?, ?)"
    cursor.execute(command_sql, (date, title, content,))
    # Guardar los cambios.
    connection.commit()
    # Cerrar la conexión a la base de datos.
    connection.close()


def get_data_blog():
    """
    Description: Recuperar todas las entradas del blog.
    """

    # Crear la conexión a la base de datos.
    connection = sqlite3.Connection("./data/blog.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Recuperar todas las entradas del blog.
    command_sql = "SELECT * FROM blog ORDER BY date DESC"
    cursor.execute(command_sql)
    results = cursor.fetchall()
    # Cerrar la conexión a la base de datos.
    connection.close()

    return results


def create_db():
    """
    Description: Crear la base de datos.
    """

    # Crear el archivo de la bases de datos.
    connection = sqlite3.Connection("./data/blog.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()

    # Crear la tabla usuarios.
    command_sql = "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, "
    command_sql += "name TEXT, password TEXT)"
    cursor.execute(command_sql)

    # Agregar el usuario principal.
    command_sql = "INSERT INTO users (username, name, password) VALUES "
    command_sql += "('agustincomolli', 'Agustín', 'admin')"
    cursor.execute(command_sql)

    # Crear la tabla del blog.
    command_sql = "CREATE TABLE blog (id INTEGER PRIMARY KEY, date DATE, "
    command_sql += "title TEXT, content TEXT)"
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


@app.route("/login", methods=["POST"])
def login():
    form = request.form
    if is_valid_user(form):
        return redirect("/")

@app.route("/login-form")
def login_form():
    with open("./static/login.html", mode="r", encoding="UTF-8") as file:
        page = file.read()
    return page


@app.route("/")
def index():
    if not os.path.exists("./data/blog.db"):
        create_db()

    with open("./templates/template.html", mode="r", encoding="UTF-8") as file:
        page = file.read()

    if session.get("login"):
        form =f"<h1>{session['name']}</h1>"
    else:
        form = create_simple_form()

    content = form + create_blog_page()

    page = page.replace("{content}", content)

    return page


app.run(host="0.0.0.0", port=81)
