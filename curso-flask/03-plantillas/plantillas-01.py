from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """ 
    Esta función controla la ruta principal ("/") y devuelve la plantilla de Flask con un solo atributo. 

    Returns: 
        render_template: HTML renderizado con los datos proporcionados como atributos.
    """

    # Este diccionario contiene los datos que se pasarán a la plantilla.
    data = {
        # El título que aparecerá en la pestaña del navegador
        "title": "Plantillas en Flask",
        # El encabezado principal que aparecerá en la página
        "h1": "Bienvenido al mundo Flask"
    }

    # Devuelve la plantilla de Flask con los datos.
    return render_template("index.html", data=data)


if __name__ == "__main__":
    """
    Este es el punto de entrada principal del programa. 
    Inicia el servidor si el script se ejecuta directamente (es decir, no se importa como un módulo).
    """

    # Ejecute la aplicación. host="0.0.0.0" hace que su servidor esté disponible en cualquier lugar,
    # no solo en su computadora. debug=True permite que la aplicación muestre errores detallados
    app.run(debug=True, host="0.0.0.0")
