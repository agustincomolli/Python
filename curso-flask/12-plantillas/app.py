from flask import Flask, request, make_response, redirect, render_template

# Crear una instancia de la aplicación Flask
app = Flask(__name__)


@app.route("/show-ip")
# Definir una ruta para mostrar la dirección IP almacenada en las cookies ("/show-ip")
def show_ip():
    """
    Función para manejar solicitudes a la ruta "/show-ip".

    Retorna un mensaje HTML que muestra la dirección IP almacenada en las cookies.
    """
    # Obtener la dirección IP almacenada en las cookies
    user_ip = request.cookies.get("user_ip")

    # Mostrar la página information.html pasando el valor user_ip.
    return render_template("information.html", user_ip=user_ip)


@app.route("/")
# Definir una ruta para la página principal ("/")
def index():
    """
    Función para manejar solicitudes a la ruta principal ("/").

    Almacena la dirección IP del usuario en las cookies y redirige a la ruta "/show-ip".
    """
    # Obtener la dirección IP del usuario que realiza la solicitud
    user_ip = request.remote_addr

    # Crear una respuesta de redirección a la ruta "/show-ip"
    response = make_response(redirect("/show-ip"))

    # Establecer una cookie llamada "user_ip" con el valor de la dirección IP del usuario
    response.set_cookie("user_ip", user_ip)

    # Retornar la respuesta de redirección
    return response


# Verificar si este script es el script principal que se está ejecutando
if __name__ == "__main__":
    # Iniciar la aplicación Flask en el host "0.0.0.0" para que sea accesible desde cualquier dirección IP
    # Habilitar el modo de depuración para facilitar la identificación y corrección de errores
    app.run(host="0.0.0.0", debug=True)
