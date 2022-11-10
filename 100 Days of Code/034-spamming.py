import os
import time


def color_me(text, color):
    """
        DESCRIPTION: Devuelve un texto, con el código del color seleccionado.\n
        PARAMETERS:\n
                    - text: es el texto a colorear
                    - color: red, green, yellow, blue, magenta o cyan.
    """
    default_color = "\033[0m"
    red_color = "\033[31m"
    green_color = "\033[32m"
    yellow_color = "\033[33m"
    blue_color = "\033[34m"
    magenta_color = "\033[35m"
    cyan_color = "\033[36m"

    if color == "red":
        color = red_color
    elif color == "green":
        color = green_color
    elif color == "blue":
        color = blue_color
    elif color == "yellow":
        color = yellow_color
    elif color == "magenta":
        color = magenta_color
    elif color == "cyan":
        color = cyan_color
    else:
        color = default_color

    return color + text + default_color


def input_color(message, color_message="", color_input=""):
    """
        DESCRIPTION: Crea un input que tiene el mensaje en color y el texto
                     de entrada en color.\n
        PARAMETERS:\n
                    - message: es el texto del mensaje al usuario.
                    - color_message y color_input: red, green, yellow, blue,
                      magenta o cyan.
    """

    default_color = "\033[0m"
    red_color = "\033[31m"
    green_color = "\033[32m"
    yellow_color = "\033[33m"
    blue_color = "\033[34m"
    magenta_color = "\033[35m"
    cyan_color = "\033[36m"

    if color_message == "red":
        color_message = red_color
    elif color_message == "green":
        color_message = green_color
    elif color_message == "blue":
        color_message = blue_color
    elif color_message == "yellow":
        color_message = yellow_color
    elif color_message == "magenta":
        color_message = magenta_color
    elif color_message == "cyan":
        color_message = cyan_color
    else:
        color_message = default_color

    if color_input == "red":
        color_input = red_color
    elif color_input == "green":
        color_input = green_color
    elif color_input == "blue":
        color_input = blue_color
    elif color_input == "yellow":
        color_input = yellow_color
    elif color_input == "magenta":
        color_input = magenta_color
    elif color_input == "cyan":
        color_input = cyan_color
    else:
        color_input = default_color

    value = input(color_message + message + color_input)
    print(default_color, end="")

    return value


def print_emails():
    os.system("clear")

    print("Lista de emails\n")
    for index, email in enumerate(list_emails):
        print(f"{index + 1} - {email}")
    print()

    time.sleep(2)


def get_spam():
    if len(list_emails) > 10:
        amount = 10
    else:
        amount = len(list_emails)

    for i in range(amount):
        os.system("clear")
        
        spam = f"Estimado {list_emails[i]}\n"
        spam += "Nos hemos dado cuenta de que se está perdiendo los " + \
            "increíbles 100 días de código de Replit. Insistimos en que " + \
            "lo hagas de inmediato. Si no lo hace, pasaremos su " + \
            "dirección de correo electrónico a todos los spammers que " + \
            "hayamos encontrado y también lo inscribiremos en el " + \
            "boletín de My Little Pony, porque eso es genial. Podríamos " + \
            "hacer eso de todos modos.\n"
        spam += "\nAmor y abrazos,\n\nIan spamington III"

        print(f"Email N° {i + 1}\n")
        print(spam)
        time.sleep(3)


list_emails = []

while True:
    os.system("clear")

    print(color_me("*** SPAMMER S.A. 📧 ***\n", "yellow"))
    text_menu = "1 - Agregar email\n2 - Eliminar email\n"
    text_menu += "3 - Ver lista de emails\n4 - Generar SPAM\n"
    text_menu += "5 - Salir\n\nIngrese su opción: "

    menu = input_color(text_menu, "", "green")

    if menu == "1":
        email = input_color("Email > ", "", "green")
        list_emails.append(email)
    elif menu == "2":
        email = input_color("Email > ", "", "green")
        if email in list_emails:
            list_emails.remove(email)
    elif menu == "3":
        print_emails()
    elif menu == "4":
        get_spam()
    elif menu == "5":
        break
