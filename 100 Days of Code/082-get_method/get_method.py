from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    arguments = request.args

    if len(request.args) > 0:
        if arguments["lang"].lower() == "en":
            return "<h1>Welcome to my web site</h1>"
    else:
        message = "<h1>Bienvenido a mi sitio web</h1>\n"
        message += "<p>Para ver este mensaje en inglés, escribe <strong>/?lang=en"
        message += "</strong> al final de la barra de direcciones</p>"
        return message

app.run(host="0.0.0.0", port=81)