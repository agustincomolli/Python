from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "title": "Reutilizando plantillas",
        "h1": "Bienvenidos a Flask"
    }

    return render_template("index.html", data=data)


@app.route("/contact")
def contact():
    data = {
        "title": "Página de contacto",
        "h1": "Bienvenidos a Flask"
    }

    return render_template("contact.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)