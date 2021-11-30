import sqlite3
import xml.etree.ElementTree as ElementTree

conexion = sqlite3.connect("track.sqlite")
cur_archivo = conexion.cursor()

cur_archivo.executescript("""
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE "Album" (
	"id"	INTEGER NOT NULL UNIQUE,
	"artist_id"	INTEGER,
	"title"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
    );

    CREATE TABLE "Artist" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
    );

    CREATE TABLE "Genre" (
        "id"	INTEGER NOT NULL UNIQUE,
        "name"	TEXT UNIQUE,
        PRIMARY KEY("id" AUTOINCREMENT)
    );

    CREATE TABLE "Track" (
	"id"	INTEGER NOT NULL UNIQUE,
	"album_id"	INTEGER,
    "genre_id" INTEGER,
	"title"	TEXT UNIQUE,
	"len"	INTEGER,
	"rating"	INTEGER,
	"count"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
    );
""")

archivo_xml = input("Ingrese el name del archivo: ")
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

    title = buscar(entrada, "Name")
    artista = buscar(entrada, "Artist")
    album = buscar(entrada, "Album")
    count = buscar(entrada, "Count")
    rating = buscar(entrada, "Rating")
    len = buscar(entrada, "Total Time")
    genero = buscar(entrada, "Genre")

    if title is None or artista is None or album is None or genero is None: 
        continue

    print(title, artista, album, genero, count, rating, len)

    cur_archivo.execute("""
        INSERT OR IGNORE INTO Artist (name) VALUES (?)
    """, (artista,))
    cur_archivo.execute("SELECT id FROM Artist WHERE name = ?", (artista,))
    artist_id = cur_archivo.fetchone()[0]

    cur_archivo.execute("""
        INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES (?, ?)""", (album, artist_id))
    cur_archivo.execute("SELECT id FROM Album WHERE title = ?", (album,))
    album_id = cur_archivo.fetchone()[0]

    cur_archivo.execute("""
        INSERT OR IGNORE INTO Genre (name) VALUES (?)
        """, (genero,))
    cur_archivo.execute("SELECT id FROM Genre WHERE name = ?", (genero,))
    genre_id = cur_archivo.fetchone()[0]

    cur_archivo.execute("""
        INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, 
        rating, count) VALUES (?, ?, ?, ?, ?, ?)
    """, (title, album_id, genre_id, len, rating, count))
    conexion.commit()

cur_archivo.execute("""
    SELECT Track.title AS "Pista", Artist.name AS "Artista", 
        Album.title AS "Album", Genre.name AS "Género"
        FROM Track JOIN Genre JOIN Album JOIN Artist
        ON Track.genre_id = Genre.id AND Track.album_id = Album.id
        AND Album.artist_id = Artist.id
        ORDER BY Artist.name, Track.title LIMIT 3
""")
lista_canciones = cur_archivo.fetchall()
print("\n")
for cancion in lista_canciones:
    title, artista, album, genero = cancion
    print(title, "-", artista, "-", album, "-", genero)