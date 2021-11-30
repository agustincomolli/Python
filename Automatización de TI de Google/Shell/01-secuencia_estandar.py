#!/usr/bin/env python3

datos = input("Esto viene de STDIN: ")
print("Ahora lo escribimos en STDOUT: " + datos)
print("Ahora generaremos un error en STDERR: " + datos + 1)

# Para redirigir la salida del programa a un archivo hay que usar en la 
# línea de comando el símbolo > nombre_archivo.

# Para anexar más información a dicho archivo (append) hay que usar el
# símbolo >> nombre_archivo.