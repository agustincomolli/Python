# En mi cuenta de Gmail, ir a Seguridad, en la sección Iniciar sesión con
# Googlez ir a Contraseñas de Aplicaciones y generar una par Gmail.
import smtplib
import schedule
import time
import random
from mylib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_credentials():
    """
    Description: Obtiene las credenciales de Gmail.
    """

    username = "user@gmail.com"
    password = ""
    
    return {"username": username, "password": password}


def send_mail():
    """
    Description: Genera y envía un correo electrónico usando la cuenta de Gmail.
    """

    # Datos del servidor
    server = "smtp.gmail.com"
    port = 587

    # Crear la conexión al servidor de email.
    connection = smtplib.SMTP(host=server, port=port)
    connection.starttls()

    credentials = get_credentials()
    quote_of_the_day = get_random_quote()

    print(f"\nEnviando cita: \"{quote_of_the_day}\"\n")

    try:
        connection.login(user=credentials["username"],
                        password=credentials["password"])
    except:
        show_error("El usuario o la contraseña no són válidos.😡")
        return

    # Crear el mensaje.
    message = MIMEMultipart()
    message["To"] = credentials["username"]
    message["From"] = credentials["username"]
    message["Subject"] = "Cita del día"
    message.attach(MIMEText(quote_of_the_day, "html"))

    try:
        # Enviar el mensaje.
        connection.send_message(message)
    except:
        show_error("El mensaje no se ha podido enviar 😭")
    else:
        print(color_me("\nMensaje enviado ✔️", "magenta"))

    # Eliminar la variable message para no consumir más RAM.
    del message
    connection.quit()


def get_random_quote():
    """
    Description: Devuelve una cita de forma aleatoria.
    """
    
    with open("./motivational_quotes.txt", mode="r", encoding="UTF-8") as file:
        quotes = file.readlines()

    return random.choice(quotes).strip()


print(color_me("Cita del día\n" + "=" * 12, "yellow"))
# Programar tarea para enviar correo electrónico cada hora
schedule.every(24).hours.do(send_mail)

while True:
    schedule.run_pending()
    # Esperar una hora.
    time.sleep(3600)
