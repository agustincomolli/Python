import sqlite3

# Mostrar un menú de opciones.
def mostrar_menu():
    opcion = 0
    
    while int(opcion) != 6:
        print("Bienvenido al sistema:")
        print("*" * 22, "\n")
        print("1 - Agregar nueva computadora.")
        print("2 - Editar una computadora.")
        print("3 - Eliminar una computadora.")
        print("4 - Ver detalles de una computadora.")
        print("5 - Mostrar la lista de computadoras.")
        print("6 - Salir.")
        
        opcion = input("\nElija una opción: ")
        
        if int(opcion) == 1:
            crear_computadora()
        elif int(opcion) == 2:
            editar_computadora()
        elif int(opcion) == 3:
            eliminar_computadora()
        elif int(opcion) == 4:
            mostrar_detalle()
        elif int(opcion) == 5:
            mostrar_lista_computadoras()
    
    
# Insertar un registro nuevo en la tabla computer.
def crear_computadora():
    print("\nAgregar nueva computadora:\n" + "*" * 26)
    nombre = input("Nombre: ")
    nucleos = int(input("Núcleos: "))
    velocidad = float(input("Velocidad GHz: "))
    memoria = int(input("RAM :"))
    costo = float(input("Costo: $ "))
    # Crear la cadena de consulta con los nuevos valores.
    insert_sql = f"INSERT INTO computer (name, cores, cpu_speed, ram, cost) "
    insert_sql += f"VALUES ('{nombre}', {nucleos}, {velocidad}, {memoria}, {costo})"
    # Ejecutar la consulta.
    conexion.execute(insert_sql)
    # Confirmar los cambios en la base de datos
    conexion.commit()


# Mostrar la lista de las computadoras.
def mostrar_lista_computadoras():
    # Ejecutar consulta.
    consulta = conexion.execute("SELECT * FROM computer")
    # Obtener los datos.
    computadoras = consulta.fetchall()
    # Mostrar la lista de computadoras.
    for computadora in computadoras:
        print(f"{computadora}")

    input("Presione ENTER para continuar...")


# Mostrar todos los datos de una computadora.
def mostrar_detalle():
    print("\nMostrar detalles de una computadora:\n" + "*" * 36)
    nombre = input("Nombre: ")
    # Ejecutar consulta.
    consulta = conexion.execute(f"SELECT * FROM computer WHERE name = '{nombre}'")
    computadora = consulta.fetchone()
    # Si encontró lo que buscaba....
    if computadora != None:
        # Mostrar los resultados.
        print(f"Núcleos: {computadora[1]}")
        print(f"Velocidad GHz: {computadora[2]}")
        print(f"RAM: {computadora[3]}")
        print(f"Costo: $ {computadora[4]}")
    else:
        # Informar que la búsqueda no dio resultados.
        print("¡La computadora que busca no está en la base de datos!")
    
    input("Presione ENTER para continuar...")


# Editar todos los datos de una computadora.
def editar_computadora():
    nombre = input("\nBuscar computadora: ")
    # Ejecutar consultade búsqueda.
    consulta = conexion.execute(f"SELECT * FROM computer WHERE name = '{nombre}'")
    computadora = consulta.fetchone()
    # Si encontró lo que buscaba...
    if computadora != None:
        # Editar la computadora.
        nombre_viejo = nombre
        print(f"\nEditar computadora: \"{nombre}\"\n" + "*" * 20)
        nombre = input("Nombre: ")
        nucleos = int(input("Núcleos: "))
        velocidad = float(input("Velocidad GHz: "))
        memoria = int(input("RAM :"))
        costo = float(input("Costo: $ "))
        # Crear la cadena de consulta con los nuevos valores.
        update_sql = f"UPDATE computer SET name = '{nombre}', cores = {nucleos}, "
        update_sql += f"cpu_speed = {velocidad}, ram = {memoria}, cost = {costo} "
        update_sql += f"WHERE name = '{nombre_viejo}'"
        # Ejecutar la consulta.
        conexion.execute(update_sql)
        # Confirmar los cambios en la base de datos
        conexion.commit()
        # Informar edición realizada.
        print("\n¡La computadora ha sido MODIFICADA!")
    else:
        # Informar que la búsqueda no dio resultados.
        print("¡La computadora no existe en la base de datos!")
    
    input("Presione ENTER para continuar...")


def eliminar_computadora():
    nombre = input("\nBuscar computadora: ")
    # Ejecutar consultade búsqueda.
    consulta = conexion.execute(f"SELECT * FROM computer WHERE name = '{nombre}'")
    computadora = consulta.fetchone()
    # Si encontró lo que buscaba...
    if computadora != None:
        # Eliminar la computadora.
        # Crear la cadena de consulta con los nuevos valores.
        delete_sql = f"DELETE FROM computer WHERE name = '{nombre}'"
        # Ejecutar la consulta.
        conexion.execute(delete_sql)
        # Confirmar los cambios en la base de datos
        conexion.commit()
        # Informar edición realizada.
        print("\n¡La computadora ha sido ELIMINADA!")
    else:
        # Informar que la búsqueda no dio resultados.
        print("¡La computadora no existe en la base de datos!")
    
    input("Presione ENTER para continuar...")

# Conectar con la base de datos.
conexion = sqlite3.connect("computer_cards.db")

mostrar_menu()

# Cerrar la conexión a la base de datos.
conexion.close()