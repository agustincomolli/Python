# La función open con el segundo parámetro indica el modo de cómo se tiene que
# arbrir un archivo: "r" = read only, "w" = write only, "a" = append, 
# "r+" = read and write.

with open("archivo_creado.txt", "w") as archivo:
    archivo.write("Esta línea será borrada pronto...")

with open("archivo_creado.txt", "w") as archivo:
    archivo.write("Era de de noche y llovía...")

with open("archivo_creado.txt") as archivo:
    print(archivo.read())
