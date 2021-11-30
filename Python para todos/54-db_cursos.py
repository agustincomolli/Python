import json
import sqlite3

conexion = sqlite3.connect("cursos.sqlite")
cur_archivo = conexion.cursor()

# Crear tablas en la base de datos.
cur_archivo.executescript("""
    DROP TABLE IF EXISTS Usuarios;
    DROP TABLE IF EXISTS Miembros;
    DROP TABLE IF EXISTS Cursos;

    CREATE TABLE Usuarios (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        nombre TEXT UNIQUE
    );

    CREATE TABLE Cursos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        titulo TEXT UNIQUE
    );

    CREATE TABLE Miembros (
        usuario_id INTEGER,
        curso_id INTEGER,
        rol INTEGER,
        PRIMARY KEY (usuario_id, curso_id)
    )
""")

nombre_archivo = input("Ingrese el nombre del archivo: ")
if len(nombre_archivo) < 1:
    nombre_archivo = "roster_data_sample.json"

archivo = open(nombre_archivo).read()
datos_json = json.loads(archivo)

for entrada in datos_json:
    nombre = entrada[0]
    titulo = entrada[1]
    rol = entrada[2]

    print((nombre, titulo, rol))

    cur_archivo.execute("""
        INSERT OR IGNORE INTO Usuarios (nombre)
        VALUES (?)""", (nombre,))
    cur_archivo.execute("SELECT id FROM Usuarios WHERE nombre = ?", (nombre,))
    usuario_id = cur_archivo.fetchone()[0]

    cur_archivo.execute("""
        INSERT OR IGNORE INTO Cursos (titulo)
        VALUES (?)""", (titulo,))
    cur_archivo.execute("SELECT id FROM Cursos WHERE titulo = ?", (titulo,))
    curso_id = cur_archivo.fetchone()[0]

    cur_archivo.execute("""
        INSERT OR REPLACE INTO Miembros (usuario_id, curso_id, rol)
        VALUES (?,?, ?)""", (usuario_id, curso_id, rol))
    
    conexion.commit()
    