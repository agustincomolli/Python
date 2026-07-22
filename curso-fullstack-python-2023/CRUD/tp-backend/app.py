from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__) # Creo la instancia de Flask

mysql = MySQL() # Creo la instancia de MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # Defino el host
app.config['MYSQL_DATABASE_PORT'] = 3306 # Defino el puerto
app.config['MYSQL_DATABASE_USER'] = 'root' # Defino el usuario
app.config['MYSQL_DATABASE_PASSWORD'] = '' # Defino la contraseña
app.config['MYSQL_DATABASE_DB'] = 'movies' # Defino la base de datos
mysql.init_app(app) # Inicializo la aplicación


@app.route('/') # Defino la ruta
def index(): # Defino la función bloque de código

    sql = "SELECT * FROM movies.movies;" # Defino la consulta

    conn = mysql.connect() # Creo la conexión
    cursor = conn.cursor() # Creo el cursor
    cursor.execute(sql) # Ejecuto la consulta

    data_movies = cursor.fetchall() # Obtengo los datos

    cursor.close() # Cierro el cursor

    return render_template('movies/index.html', jinja_html_movies=data_movies) # Retorno el template

if __name__ == '__main__':
    app.run(debug=True) # Ejecuto la aplicación en modo debug