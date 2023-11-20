from flask import Flask, render_template, request

app = Flask(__name__)


@app.before_request
def before_request():
    print("Antes de la petición")


# Esta función se ejecuta después de cada solicitud al servidor. Es útil para
# acciones que deben llevarse a cabo independientemente del resultado de las
# vistas, como cerrar conexiones a base de datos, liberar recursos o agregar
# encabezados HTTP a las respuestas. En este ejemplo, simplemente imprime un
# mensaje y luego devuelve la respuesta sin modificar.
@app.after_request
def after_request(response):  # Siempre debe tener un parámetro
    print("Después de la petición")
    return response  # Siempre se debe devolver la respuesta


@app.route("/")
def index():
    print("Realizando la petición...")
    title = "Curso de Flask"
    return render_template("index.html", title=title)


@app.route("/contact")
def contact():
    title = "Curso de Flask"
    return render_template("contact.html", title=title)


@app.route("/greet/<name>")
# Los parámetros se pasan entre los símbolos <>.
def greets(name: str):
    return f"¡Hola {name.capitalize()}!"


@app.route("/sum/<int:number_1>/<int:number_2>")
# Para pasar parámetros numéricos hay que agregar antes int:
def sum(number_1: int, number_2: int):
    # Siempre se debe devolver un string.
    return f"La suma de {number_1} + {number_2} es: {number_1 + number_2}"


@app.route("/profile/<name>/<int:age>")
def profile(name: str, age: int):
    return f"Hola, tu nombre es {name} y tienes {age} años."


@app.route("/languages")
def languages():
    title = "Curso de Flask"
    data = {
        "has_languages": True,
        "languages": ["HTML", "CSS", "JavaScript", "Python"]
    }
    return render_template("languages.html", title=title, data=data)


# Este decorador dirige una URL '/data' a la función Python de abajo
@app.route("/data")
def data():
    # Se utiliza el objeto request para obtener parámetros de la URL como 'name'
    name = request.args.get("name")
    age = request.args.get("age")
    # Se devuelve una cadena de texto formateada con los datos obtenidos de la URL
    return f"Estos son los datos: {name} y {age}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
