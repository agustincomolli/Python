from flask import Flask


def create_entry(heading, date, text):
    """
    Description: Crea una entrada de blog, tomando la plantilla HTML y 
                 reemplaza los valores por los parámetros.
    Return:      Devuelve un archivo con el contenido HTML para renderizar.
    """
    with open("./template/template.html", mode="r", encoding="UTF-8") as file:
        page = file.read()
    page = page.replace("{heading}", heading)
    page = page.replace("{date}", date)
    page = page.replace("{text}", text)

    return page


app = Flask(__name__, static_url_path="/static")


@app.route("/")
def index():
    heading = "Entradas"
    date = ""
    text = "<p><a href='/one'>Una entrada</a></p>"
    text += "<p><a href='/two'>Otra entrada</a></p>"

    return create_entry(heading, date, text)


@app.route("/one")
def one():
    heading = "Ahorcado"
    date = "10/12/2022"
    text = "Este proyecto es el juego del ahorcado escrito en Python. "
    text += "El juego elige una palabra al azar de una lista de palabras "
    text += "y luego pide al usuario que adivine las letras una por una. "
    text += "Si el usuario adivina una letra correctamente, se muestra la "
    text += "letra en su lugar en la palabra oculta. Si el usuario elige "
    text += "una letra incorrecta, se le resta una vida. El juego continúa "
    text += "hasta que el usuario adivine la palabra o se quede sin vidas."

    return create_entry(heading, date, text)


@app.route("/two")
def two():
    heading = "¿Quién es Quién?"
    date = "20/12/2022"
    text = "Este proyecto es un juego que consiste en adivinar qué imagen "
    text += "se está mostrando en la pantalla. El usuario debe ingresar el "
    text += "nombre de la imagen en una caja de texto y presionar el botón "
    text += "\"Buscar\". Si la entrada del usuario es correcta, se mostrará "
    text += "una nueva imagen y el usuario debe seguir adivinando. Si la "
    text += "entrada es incorrecta o si el usuario llega a la última imagen "
    text += "y no ha adivinado correctamente, se mostrará un mensaje de que "
    text += "ha perdido y se habilitará un botón para reiniciar el juego. "
    text += "Si el usuario adivina correctamente la última imagen, se mostrará "
    text += "un mensaje de que ha ganado y también se habilitará un botón "
    text += "para reiniciar el juego."

    return create_entry(heading, date, text)


app.run(host="0.0.0.0", port=81)
