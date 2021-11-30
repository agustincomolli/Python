# Leer un archivo.

# Abrir el archivo en un objeto como solo lectura "r".
archivo = open("./un_archivo.txt", "r")
# Leer el contenido del archivo.
datos_archivo = archivo.read()
# Cerrar el archivo para liberar recursos.
archivo.close()

print(datos_archivo)

# Escribir en un archvio.

# Abrir un archivo en modo escritura. Si existe se eliminará
# todo su contenido.
archivo = open("./otro_archivo.txt", "w")
datos_archivo = archivo.write("Hola por ahí")
archivo.close()
