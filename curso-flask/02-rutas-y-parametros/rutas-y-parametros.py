from flask import Flask, request


app = Flask(__name__)


@app.route("/")
@app.route("/<name>/")
@app.route("/<name>/<last_name>/<age>")
def greets(name: str = "", last_name: str = "", age: int = 0):
    if name != "" and last_name != "" and age != 0:
        message = f"¡Hola, {name} {last_name}! Tienes {age} años de edad."
    elif name != "" and last_name != "":
        message = f"¡Hola, {name} {last_name}!"
    elif name != "" and last_name == "":
        message = f"¡Hola, {name}!"
    else:
        message = "Escribe una '/' al final de la dirección y pon tu nombre para "
        message += "saludarte mejor. También puedes pasar más datos como tu"
        message += "apellido y edad (esta última en formato de número)."
        message += "<br><br>Ejemplos:<br>http://192.168.2.199:5000/Agustín/"
        message += "<br>http://192.168.2.199:5000/Agustín/Comolli"
        message += "<br>http://192.168.2.199:5000/Agustín/Comolli/46"

    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
