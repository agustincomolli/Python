import sqlite3

# Conectar a la base de datos.
conexion = sqlite3.connect("computer_cards.db")
# Ejecutar consulta.
datos = conexion.execute("SELECT * FROM computer")
# Recuperar los datos.
computadoras = datos.fetchall()

for computadora in computadoras:
    # Imprimir el nombre de la computadora
    print(computadora[0])

# Cerrar la conexión a la base de datos.
conexion.close()