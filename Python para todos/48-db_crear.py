import sqlite3

# Crear la conexión a la base de datos. Si el archivo
# no existe se creará.
conexion = sqlite3.connect("musica.sqlite")
# El cursor es un objeto con el que podemos realizar operaciones en
# los datos almacenados.
cur_archivo = conexion.cursor()

cur_archivo.execute("DROP TABLE IF EXISTS Pistas")
cur_archivo.execute("CREATE TABLE Pistas (titulo TEXT, reproducidas INTEGER)")

# Insertar valores.
cur_archivo.execute("INSERT INTO Pistas (titulo, reproducidas) VALUES (?, ?)", ("Thunderstruck", 20))
cur_archivo.execute("INSERT INTO Pistas (titulo, reproducidas) VALUES (?, ?)", ("My Way", 15))
# Forzar que los datos se escriban en el archivo.
conexion.commit()

# Actualizar un valor.
cur_archivo.execute("UPDATE Pistas SET reproducidas = 16 WHERE titulo = 'My Way'")

# Mostrar los datos
print("Pistas: ")
cur_archivo.execute("SELECT titulo, reproducidas FROM Pistas")
for registro in cur_archivo:
    print(registro)

cur_archivo.execute("DELETE FROM Pistas WHERE reproducidas < 100")
conexion.commit()

conexion.close()