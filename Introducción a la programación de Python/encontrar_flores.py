# Escribe tu código aquí
# SUGERENCIA: crea un diccionario a partir de flowers.txt
def crear_diccionario(nombrearchivo):
    dict_flores = {}
    with open(nombrearchivo) as archivo:
        for linea in archivo:
            flor = linea.split(sep=":")
            dict_flores[flor[0]] = flor[1].strip()
        return dict_flores


# SUGERENCIA: cree una función para solicitar el nombre y apellido del usuario
def main():
    nombre = input("Ingrese su primer [espacio] Apellido solamente: ")
    # imprime la salida deseada
    flores = crear_diccionario("./flores.txt")
    print(f"Nombre único de la flor con la primera letra: {flores[nombre[0]]}")


main()