from flask import Flask, request

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir una ruta para la página principal "/"
@app.route("/")
def index():
    """
    Función para manejar solicitudes a la ruta principal ("/").
    
    Retorna un mensaje HTML que saluda al usuario y muestra su dirección IP.
    """
    # Obtener la dirección IP del usuario que realiza la solicitud
    user_ip = request.remote_addr
    
    # Construir el mensaje HTML que se mostrará en la página
    message = "<h1>¡Hola mundo!</h1>"
    message += f"<p>Tu dirección IP es <strong>{user_ip}</strong></p>"
    
    # Retornar el mensaje como respuesta a la solicitud
    return message

# Verificar si este script es el script principal que se está ejecutando
if __name__ == "__main__":
    # Iniciar la aplicación Flask en el host "0.0.0.0" para que sea accesible desde cualquier dirección IP
    # Habilitar el modo de depuración para facilitar la identificación y corrección de errores
    app.run(host="0.0.0.0", debug=True)
