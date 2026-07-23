# 10-1. Aprendiendo Python: abra un archivo en blanco en su editor de texto y 
# escriba unas pocas líneas que resuman lo que ha aprendido sobre Python 
# hasta ahora. Comience cada línea con la frase In Python you can.... Guarde 
# el archivo como learning_python.txt en el mismo directorio que sus 
# ejercicios de este capítulo. Escriba un programa que lea el archivo e 
# imprima lo que escribió tres veces. Imprima el contenido una vez leyendo 
# todo el archivo, una vez recorriendo el objeto del archivo y una vez 
# almacenando las líneas en una lista y luego trabajando con ellas fuera 
# del bloque with.

# 10-2. Aprendiendo C: puede usar el método replace() para reemplazar 
# cualquier palabra en una cadena con una palabra diferente. Aquí hay un 
# ejemplo rápido que muestra cómo reemplazar 'perro' con 'gato' en una 
# oración:
# >>> mensaje = "Me gustan mucho los perros".
# >>> mensaje.reemplazar('perro', 'gato')
# Me gustan mucho los gatos.
# Lea cada línea del archivo que acaba de crear, learning_python.txt, y 
# reemplace la palabra Python con el nombre de otro idioma, como C. Imprima 
# cada línea modificada en la pantalla.

nombre_archivo = "24-aprendiendo_python.txt"

print("Ejercicio 10-1:\n" + "*" * 15)
print("\nLeyendo todo el archivo...")

with open(nombre_archivo, encoding="UTF-8") as archivo:
    contenido = archivo.read()
    print(contenido)

print("\nLeyendo lína por línea:")
with open(nombre_archivo, encoding="UTF-8") as archivo:
    for linea in archivo:
        print(linea.rstrip())

print("\nLeyendo y trabajando fuera del bloque with:")
with open(nombre_archivo, encoding="UTF-8") as archivo:
    lineas = archivo.readlines()

for linea in lineas:
    # Ejercicio 10-2.
    print(linea.replace("Python", "Visual Basic").rstrip())