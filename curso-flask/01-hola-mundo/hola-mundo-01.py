# Importamos el módulo Flask de la librería flask. Flask es una librería en 
# Python para desarrollar aplicaciones web.
from flask import Flask

# Creamos una instancia de la clase Flask. "app" es la aplicación principal 
# que será utilizada y ejecutada por el servidor.
# El argumento "__name__" en el constructor Flask es una variable Python 
# predefinida, que es seteada como el nombre del módulo en el que se usa.
app = Flask(__name__)

# Usamos el decorador @app.route, que le dice a Flask qué URL debería activar 
# nuestra función.
# En este caso, el route "/" significa que la función greets será ejecutada 
# cuando visitemos la página principal (por ejemplo: http://localhost:5000/)


@app.route("/")
# Definimos la función greets que se activará cuando visitemos la URL "/".
# Cuando accedes a esa URL, esta función devolverá el string "¡Hola mundo!".
def greets():
    return "¡Hola mundo!"
