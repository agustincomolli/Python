import sqlite3

conexion = sqlite3.connect("dominios.sqlite")
cur_archivo = conexion.cursor()

# Borrar la tabla Recuentos y su contenido.
cur_archivo.execute("DROP TABLE IF EXISTS Recuentos")
# Crear tabla
cur_archivo.execute("CREATE TABLE Recuentos (dominio TEXT, cuenta INTEGER)")

nombre_archivo = input("Ingrese el nombre de archivo: ")
if len(nombre_archivo) < 1: nombre_archivo = "mbox-short.txt"

try:
    archivo = open(nombre_archivo, mode="r")
except:
    print("ERROR: Archivo no disponible.")
    quit()

for linea in archivo:
    # Recorrer el archivo buscando las líneas "From: "
    if not linea.startswith("From: "): continue
    # Extraer la dirección de correo electrónico.
    palabras = linea.split()
    correo = palabras[1]
    dominio = correo.split("@")[1]
    cur_archivo.execute("SELECT cuenta FROM Recuentos WHERE dominio = ?", (dominio,))
    registro = cur_archivo.fetchone()
    if registro is None:
        # Agregarla a la base de datos si no está.
        cur_archivo.execute("INSERT INTO Recuentos (dominio, cuenta) VALUES (?, 1)", (dominio,))
    else:
        # Actualizar la cantidad de veces que aparece en el archivo.
        cur_archivo.execute("UPDATE Recuentos SET cuenta = cuenta + 1 WHERE dominio = ?", (dominio,))

conexion.commit()

# Seleccionar los 10 correos que más veces aparecen y mostrarlos.
sql_comando = "SELECT dominio, cuenta FROM Recuentos ORDER BY cuenta DESC LIMIT 10"
for registro in cur_archivo.execute(sql_comando):
    print(f"Correo: {registro[0]}, cantidad: {registro[1]}")

conexion.close()
