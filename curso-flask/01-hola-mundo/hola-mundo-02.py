# Se importa la clase Flask desde el módulo flask.
# Flask es una librería en Python para desarrollar aplicaciones web.
from flask import Flask

# Se crea una nueva instancia de la aplicación Flask.
# __name__ es una variable global en Python que representa el nombre del módulo actual.
# Pasamos __name__ al constructor Flask para que pueda ubicar los recursos de la aplicación.
app = Flask(__name__)

# La anotación @app.route registra la función index() como un manejador
# para la ruta '/' en la aplicación.


@app.route("/")
def index():
    """
    Función para manejar las solicitudes a la ruta raíz ("/").
    Devuelve un string que será mostrado en la página web.
    """
    # Devuelve un string que es un fragmento de HTML.
    # Cuando se accede a la ruta "/", esto se mostrará en el navegador web.
    return "<h1>Bienvenido a Python Flask 😎</h1>"


# Este condicional verifica si este archivo (módulo) es el que se está ejecutando
# directamente (es decir, no ha sido importado desde otro código de Python).
# Si es así, entonces se arranca el servidor Flask para la aplicación.
if __name__ == "__main__":
    # Arranca el servidor Flask que escucha las solicitudes en localhost 127.0.0.1,
    # puerto 5000 por defecto. Cuando una solicitud llegue para la ruta "/",
    # Flask responderá con el resultado de la función index().
    #
    # La opción debug=True activa el modo de depuración, en el que Flask muestra
    # errores detallados en el navegador si algo sale mal. Además, reinicia
    # automáticamente el servidor cada vez que se realizar cambios en el código.
    #
    # Con host="0.0.0.0" el servidor será accesible también en la red, no solamente desde
    # tu ordenador localmente. Esto significa que tu aplicación será
    # visible públicamente en internet (si tu equipo está conectado a internet y
    # no tiene activado un firewall que bloquee las conexiones). Si no se
    # especifica un host, Flask escucha solamente en localhost.
    app.run(debug=True, host="0.0.0.0")
