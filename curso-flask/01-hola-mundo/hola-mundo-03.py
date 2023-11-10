# Importamos la clase Flask y la función render_template desde el paquete de flask.
# Flask es un microframework web, usado para hacer aplicaciones web.
# render_template es una función que renderiza un template (plantilla) y lo devuelve
# con los datos apropiados inyectados, creando así una respuesta completa.
from flask import Flask, render_template

# Creamos una instancia de la clase Flask que será nuestra aplicación.
# Pasamos __name__ al constructor de la app para que Flask sepa donde buscar
# recursos, como templates y archivos estáticos.
app = Flask(__name__)

# Aquí usamos el decorador @app.route para asociar URL a funciones de Python.
# En este caso, estamos asociando la URL raíz ("/") a la función index().


@app.route("/")
def index():
    """
    Esta es la función que manejará la petición a la raíz del sitio.
    Retorna el template HTML index.html que se encuentra en la carpeta de templates.
    La función render_template tomará este archivo, lo procesará y devolverá el 
    resultado como una cadena de texto HTML para ser enviado como respuesta.
    """
    return render_template("index.html")


# Este condicional verifica si este script es el que se ha ejecutado directamente.
# Si es así, arranca el servidor de la aplicación. Si este script ha sido
# importado desde otro módulo, no hará nada, lo que es común para prevenir
# que se ejecute la aplicación cuando no se desea.
if __name__ == "__main__":
    # Arranca el servidor de Flask en modo debug (muestra información de diagnóstico
    # útil en el navegador si ocurre un error) y permite conexiones desde cualquier host.
    app.run(debug=True, host="0.0.0.0")
