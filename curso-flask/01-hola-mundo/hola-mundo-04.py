"""
En términos de parámetros de URL, estos son los pequeños fragmentos de 
información que agregas al final de la URL después de un signo de 
interrogación. En el contexto de Flask, puedes recoger estos parámetros usando 
request.args.get. En el código proporcionado, por ejemplo, puedes usar 
http://localhost:5000/?name=ChatGot la aplicación Flask te saludará con 
“¡Hola, ChatGot!”, sino solo verás “¡Hola, Usuario!”.

"""

from flask import Flask
# Importa el objeto request para tratar las solicitudes HTTP.
from flask import request


app = Flask(__name__)


@app.route("/")
def index():
    # Desde request.args se puede acceder a los parámetros de la URL como 
    # diccionario.
    # En este caso, intenta obtener el parámetro "name", y si no está presente, 
    # tiene un valor predeterminado de "Usuario".
    name = request.args.get("name", "Usuario")
    return f"¡Hola, {name}!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
