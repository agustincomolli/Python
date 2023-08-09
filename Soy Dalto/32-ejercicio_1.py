# Hay dos listas: una contiene nombres y la otra apellidos.
# Guardar los datos en un archivo txt, de modo que a cada nombre
# le corresponda su apellido"

first_names = ["Agustín", "Lorena", "Carlos", "Adrián", "Marcela", "Gabriela"]
last_names = ["Comolli", "Mellado", "Giola", "Gomez", "Faure", "Zanaboni"]

with open("./nombres_apellidos.txt", mode="a", encoding="UTF-8") as file:
    for first_name, last_name in zip(first_names, last_names):
        file.write(f"{first_name} {last_name}\n")

print("Datos guardados en nombres_apellidos.txt")
