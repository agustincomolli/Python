import sys


def cowsay(message: str):
    """
    Imprime un mensaje en una burbuja de diálogo junto a la imagen de una vaca.

    :param message: Mensaje que se mostrará en la burbuja de diálogo.
    """
    
    # Imagen de la vaca en formato de arte ASCII
    cow = ""
    cow += "\n        \   ^__^"
    cow += "\n         \  (oo)\_______"
    cow += "\n            (__)\       )\/\\"
    cow += "\n                ||----w |"
    cow += "\n                ||     ||"
    cow += "\n"

    # Dividir el mensaje en líneas.
    lines = message.split("\n")
    # Establecer la longitud máxima de la línea.
    max_lenght = max(len(line) for line in lines)
    # Crear la burbuja del mensaje
    to_say = f"\n {"-" * (max_lenght + 2)}"
    to_say += f"\n< {message} >"
    to_say += f"\n {"-" * (max_lenght + 2)}"
    print(to_say, cow)


if __name__ == "__main__":
    # Verificar si se porporcionó un argumento a la línea de comando.
    if len(sys.argv) != 2:
        cowsay("Uso: python cowsay.py 'mensaje'")
        sys.exit(1)

    # Obtener el mensaje del argumento de línea de comandos
    message = sys.argv[1]
    # Llamar a la función cowsay con el mensaje proporcionado
    cowsay(message)
