from flask import Flask, request, redirect, session
from datetime import datetime
import sqlite3
import os


def insert_blog_entry(date:datetime, title:str, content:str):
    # Crear la conexión a la base de datos.
    connection = sqlite3.Connection("./data/blog.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Agregar la entrada al blog.
    command_sql = "INSERT INTO blog (date, title, content) VALUES (?, ?, ?)"
    cursor.execute(command_sql, (date, title, content,))
    # Guardar los cambios.
    connection.commit()
    # Cerrar la conexión a la base de datos.
    connection.close()


def load_blog():
    """
    Description: Recuperar todas las entradas del blog.
    """

    # Crear la conexión a la base de datos.
    connection = sqlite3.Connection("./data/blog.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()
    # Recuperar todas las entradas del blog.
    command_sql = "SELECT * FROM blog ORDER BY date DESC"
    cursor.execute(command_sql)
    results = cursor.fetchall()
    # Cerrar la conexión a la base de datos.
    connection.close()

    return results


def create_db():
    """
    Description: Crear la base de datos.
    """
    # Crear el archivo de la bases de datos.
    connection = sqlite3.Connection("./data/blog.db")
    # Crear el cursor a la base de datos.
    cursor = connection.cursor()

    # Crear la tabla usuarios.
    command_sql = "CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, "
    command_sql += "name TEXT, password TEXT)"
    cursor.execute(command_sql)

    # Agregar el usuario principal.
    command_sql = "INSERT INTO users (username, name, password) VALUES "
    command_sql += "('agustincomolli', 'Agustín', 'admin')"
    cursor.execute(command_sql)

    # Crear la tabla del blog.
    command_sql = "CREATE TABLE blog (id INTEGET PRIMARY KEY, date DATETIME, "
    command_sql += "title TEXT, content TEXT)"
    cursor.execute(command_sql)
    
    # Guardar los cambios.
    connection.commit()
    # Cerrar la conexión a la base de datos.
    connection.close()


if not os.path.exists("./data/blog.db"):
    create_db()

blog_date = input("Fecha: ")
title = input("Título: ")
content = input("Contenido: ")

blog_date = datetime.strptime(blog_date, "%d-%m-%Y")
blog_date = blog_date.date()

insert_blog_entry(blog_date, title, content)

blog = load_blog()

print(blog)