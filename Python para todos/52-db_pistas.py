import sqlite3
import xml.etree.ElementTree as ElementTree

conexion = sqlite3.connect("pistas.sqlite")
cur_archivo = conexion.cursor()

cur_archivo.executescript("""
    DROP TABLE IF EXISTS Albums;
    DROP TABLE IF EXISTS Artistas;
    DROP TABLE IF EXISTS Generos;
    DROP TABLE IF EXISTS Pistas;

    CREATE TABLE "Albums" (
	"id"	INTEGER NOT NULL UNIQUE,
	"artista_id"	INTEGER,
	"nombre"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
    );

    CREATE TABLE "Artistas" (
	"id"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
    );

    CREATE TABLE "Generos" (
        "id"	INTEGER NOT NULL UNIQUE,
        "nombre"	TEXT UNIQUE,
        PRIMARY KEY("id" AUTOINCREMENT)
    );

    CREATE TABLE "Pistas" (
	"id"	INTEGER NOT NULL UNIQUE,
	"album_id"	INTEGER,
    "genero_id" INTEGER,
	"titulo"	TEXT UNIQUE,
	"duracion"	INTEGER,
	"clasificacion"	INTEGER,
	"contador"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
    );
""")

archivo_xml = input("Ingrese el nombre del archivo: ")
if len(archivo_xml) < 1: archivo_xml = "Library.xml"

def buscar(registro, campo_a_buscar):
    encontrado = False
    for campo in registro:
        if encontrado: return campo.text
        if campo.tag == "key" and campo.text == campo_a_buscar:
            encontrado = True


arbol_xml = ElementTree.parse(archivo_xml)
datos_xml = arbol_xml.findall("dict/dict/dict")
print("Cantidad de diccionarios", len(datos_xml))

for entrada in datos_xml:
    if (buscar(entrada, "Track ID")) is None: continue

    titulo = buscar(entrada, "Name")
    artista = buscar(entrada, "Artist")
    album = buscar(entrada, "Album")
    contador = buscar(entrada, "Count")
    clasificacion = buscar(entrada, "Rating")
    duracion = buscar(entrada, "Total Time")
    genero = buscar(entrada, "Genre")

    if titulo is None or artista is None or album is None or genero is None: 
        continue

    print(titulo, artista, album, genero, contador, clasificacion, duracion)

    cur_archivo.execute("""
        INSERT OR IGNORE INTO Artistas (nombre) VALUES (?)
    """, (artista,))
    cur_archivo.execute("SELECT id FROM Artistas WHERE nombre = ?", (artista,))
    artista_id = cur_archivo.fetchone()[0]

    cur_archivo.execute("""
        INSERT OR IGNORE INTO Albums (nombre, artista_id)
        VALUES (?, ?)""", (album, artista_id))
    cur_archivo.execute("SELECT id FROM Albums WHERE nombre = ?", (album,))
    album_id = cur_archivo.fetchone()[0]

    cur_archivo.execute("""
        INSERT OR IGNORE INTO Generos (nombre) VALUES (?)
        """, (genero,))
    cur_archivo.execute("SELECT id FROM Generos WHERE nombre = ?", (genero,))
    genero_id = cur_archivo.fetchone()[0]

    cur_archivo.execute("""
        INSERT OR REPLACE INTO Pistas (titulo, album_id, genero_id, duracion, 
        clasificacion, contador) VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, album_id, genero_id, duracion, clasificacion, contador))
    conexion.commit()

cur_archivo.execute("""
    SELECT Pistas.titulo AS "Pista", Artistas.nombre AS "Artista", 
        Albums.nombre AS "Album", Generos.nombre AS "Género"
        FROM Pistas JOIN Generos JOIN Albums JOIN Artistas
        ON Pistas.genero_id = Generos.id AND Pistas.album_id = Albums.id
        AND Albums.artista_id = Artistas.id
        ORDER BY Artistas.nombre, Pistas.titulo LIMIT 3
""")
lista_canciones = cur_archivo.fetchall()
print("\n")
for cancion in lista_canciones:
    titulo, artista, album, genero = cancion
    print(titulo, "-", artista, "-", album, "-", genero)