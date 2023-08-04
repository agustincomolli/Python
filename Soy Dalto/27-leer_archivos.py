# Abrir un archivo.
file = open("./archivo.txt", encoding="UTF-8")
# Cargar su contenido.
file_content = file.read()
print(file_content)

file = open("./archivo.txt", encoding="UTF-8")
line = file.readline()
print(f"\n{line}")

# Cerrar el archivo.
file.close()

# Leer archivos de forma óptima.
with open("./archivo.txt", encoding="UTF-8") as file:
    file_content = file.read()
    print(file_content.rstrip())
    print("\nEl archivo se cerró de forma automática.")