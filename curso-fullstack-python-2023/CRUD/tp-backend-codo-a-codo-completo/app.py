from flask import Flask # Importamos la clase Flask desde el paquete flask
from flask import render_template # Metodo para renderizar templates
from flask import request # Metodo para obtener datos de los formularios
from flaskext.mysql import MySQL # Importamos la clase MySQL desde el paquete flaskext

app = Flask(__name__) # Instancia de la clase Flask

mysql = MySQL() # Instancia de la clase MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost' # Configuramos el host de la base de datos
app.config['MYSQL_DATABASE_PORT'] = 3306 # Configuramos el puerto de la base de datos
app.config['MYSQL_DATABASE_USER'] = 'root' # Configuramos el usuario de la base de datos
app.config['MYSQL_DATABASE_PASSWORD'] = '' # Configuramos la contraseña de la base de datos
app.config['MYSQL_DATABASE_DB'] = 'movies' # Configuramos el nombre de la base de datos
mysql.init_app(app) # Inicializamos la base de datos

@app.route('/') # Creamos la ruta para el index
def index():

    sql = 'SELECT id, title, lenght, created_at, update_at FROM movies.movies;' # Consulta SQL

    conn = mysql.connect() # Conexión a la base de datos
    cursor = conn.cursor() # Cursor de la base de datos
    cursor.execute(sql) # Ejecutamos la consulta

    data_movies = cursor.fetchall() # Obtenemos los datos de la consulta

    cursor.close() # Cierro el cursor

    return render_template('movies/index.html', data_jinja_movies=data_movies) # Renderizamos el template

@app.route('/create') # Creamos la ruta para crear peliculas
def create(): # Función para renderizar el template/html de crear peliculas
    return render_template('movies/create.html')


@app.route('/store', methods=['POST']) # Creamos la ruta para almacenar peliculas
def store(): # Función para almacenar peliculas
     title = request.form['title'] # Obtenemos el titulo de la pelicula
     length = request.form['length'] # Obtenemos la duración de la pelicula
     
     sql = "INSERT INTO `movies`.`movies` (`title`,`lenght`,`created_at`) VALUES ('" + title + "'," + length + ",NOW());" # Consulta SQL

     conn = mysql.connect() # Conexión a la base de datos
     cursor = conn.cursor() # Cursor de la base de datos
     cursor.execute(sql) # Ejecutamos la consulta
     conn.commit() # Guardamos los cambios

     return "Pelicula creada con exito" # Retornamos un mensaje de exito

@app.route('/delete/<id>') # Creamos la ruta para eliminar peliculas
def delete(id):

    sql = "DELETE FROM `movies`.movies where id = " + id + ";" # Consulta SQL
    conn = mysql.connect() # Conexión a la base de datos
    cursor = conn.cursor() # Cursor de la base de datos
    cursor.execute(sql) # Ejecutamos la consulta
    conn.commit() # Guardamos los cambios

    return "Pelicula elimina con exito " + id # Retornamos un mensaje de exito

@app.route('/edit/<id>') # Creamos la ruta para crear peliculas
def edit(id): # Función para renderizar el template/html de crear peliculas

    sql = "SELECT * FROM `movies`.movies WHERE id = " + id + ";"
    conn = mysql.connect() # Conexión a la base de datos
    cursor = conn.cursor() # Cursor de la base de datos
    cursor.execute(sql) # Ejecutamos la consulta

    data_one_movie = cursor.fetchone() # Obtenemos los datos de la consulta
    conn.commit() # Guardamos los cambios

    return render_template('movies/edit.html', data_jinja_one_movie=data_one_movie) # Renderizamos el template

@app.route('/update/<id>', methods=['POST']) 
def update(id): # Función para renderizar el template/html de crear peliculas
     title = request.form['title'] # Obtenemos el titulo de la pelicula
     length = request.form['length'] # Obtenemos la duración de la pelicula
     
     sql = "UPDATE `movies`.movies SET title = '" + title + "', lenght = " + length + ",update_at = NOW() WHERE id = " + id + ";" # Consulta SQL

     conn = mysql.connect() # Conexión a la base de datos
     cursor = conn.cursor() # Cursor de la base de datos
     cursor.execute(sql) # Ejecutamos la consulta
     conn.commit() # Guardamos los cambios

     return "Pelicula actualizada con exito: " + title # Retornamos un mensaje de exito

if __name__ == '__main__':
    app.run(debug=True, port=8000) # Ejecutamos el servidor en el puerto 8000