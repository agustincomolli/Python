from flask import Flask, request


def is_valid(login: dict):
    valid_logins = {}
    valid_logins["agustincomolli"] = {
        "email": "agustincomolli@yahoo.com.ar",
        "password": "Ch1ng0l@"
    }
    valid_logins["lormelmir"] = {
        "email": "lormelmir@gmail.com",
        "password": "milk&mocha"
    }
    valid_logins["carlinhos24"] = {
        "email": "carlinhos24@hotmail.com",
        "password": "camboriu"
    }

    valid = False

    if login["user"] in valid_logins:
        print("Usuario: OK")
        details = valid_logins[login["user"]]
        if login["email"] == details["email"] and login["password"] == details["password"]:
            print("Email: OK")
            print("Contraseña: OK")
            valid = True

    return valid


app = Flask(__name__, static_url_path="/static")


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
