from urllib.request import urlopen
import urllib.error
import ssl
import sqlite3
import json
import twurl

api_twitter = "https://api.twitter.com/1.1/friends/list.json"
conexion_bd = sqlite3.connect("spidering_twitter.sqlite")
cur_archivo = conexion_bd.cursor()

cur_archivo.execute("""
    CREATE TABLE IF NOT EXISTS Twitter
    (nombre TEXT, recuperados INTEGER, amigos INTEGER)
    """)

# Ignorar errores de certificados SSL
contexto = ssl.create_default_context()
contexto.check_hostname = False
contexto.verify_mode = ssl.CERT_NONE

while True:
    cuenta = input("Ingrese una cuenta de Twitter o 'salir': ")
    if cuenta == "salir": break
    if len(cuenta) < 1:
        cur_archivo.execute("SELECT nombre FROM Twitter WHERE recuperados = 0 LIMIT 1")
        try:
            cuenta = cur_archivo.fetchone()[0]
        except:
            print("No se encontraron cuentas de Twitter no recuperadas")
            continue

    url = twurl.augment(api_twitter, {'screen_name': cuenta, 'count': '20'})
    print("Recuperando....", url)
    conexion_url = urlopen(url, context=contexto)
    datos_url = conexion_url.read().decode()
    cabeceras = dict(conexion_url.getheaders())

    print("Restantes...", cabeceras["x-rate-limit-remaining"])
    datos_json = json.loads(datos_url)

    cur_archivo.execute("UPDATE Twitter SET recuperados = 1 WHERE nombre = ?", (cuenta,))

    contar_nuevo = 0
    contar_viejo = 0
    for usuario in datos_json["users"]:
        amigo = usuario["screen_name"]
        print(amigo)
        cur_archivo.execute("SELECT amigos FROM Twitter WHERE nombre = ? LIMIT 1", (amigo,))

        try:
            contar = cur_archivo.fetchone()[0]
            cur_archivo.execute("UPDATE Twitter SET amigos = ? WHERE nombre = ?", (contar + 1, amigo))
            contar_viejo += 1
        except:
            cur_archivo.execute("INSERT INTO Twitter (nombre, recuperados, amigos) VALUES (?, 0, 1)", \
                (amigo,))
            contar_nuevo += 1
        
        print("Nuevas cuentas =", contar_nuevo, " revisados =", contar_viejo)
        conexion_bd.commit()

cur_archivo.close()