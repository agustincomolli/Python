# Abrir un archivo y escribir información en él.
def write_file():
    with open("./archivo.txt", mode="a", encoding="UTF-8") as file:
#                                    |-> Append agrega contenido nuevo sin
#                                        sobreescribir el contenido anterior.
        new_content  = "\nEsta es una nueva línea de texto."
        file.write(new_content)
        new_content = "\nAquí hay otra línea nueva para completar."
        file.write(new_content)

# Mostrar el contenido del archivo.
def show_file():
    with open("./archivo.txt", mode= "r", encoding="UTF-8") as file:
        file_content = file.read()
        print(file_content)


print("Contenido del archivo:")
show_file()
write_file()
print("\nNuevo contenido del archivo:")
show_file()