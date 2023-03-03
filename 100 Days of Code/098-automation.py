# En mi cuenta de Gmail, ir a Seguridad, en la sección Iniciar sesión con
# Googlez ir a Contraseñas de Aplicaciones y generar una par Gmail.
import smtplib
import schedule
import time
from mylib import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def compose_email():
    clear_screen()
    print(color_me("Enviar email 📧\n", "yellow"))
    to = input_color("Para: ", "green")
    subject = input_color("Asunto: ", "green")
    content = input("Mensaje: ")

    return {"to": to, "subject": subject, "content": content}


def login():
    """
    Description: Inicia sesión en Gmail.
    """

    clear_screen()
    print(color_me("Enviar email 📧 - Iniciar sesión 🔐\n", "yellow"))
    username = input_color("Usuario: ", "green")
    password = input_color("Contraseña: ", "green")

    return {"username": username, "password": password}


def send_mail(credentials: dict, email: dict):
    """
    Description: Genera y envía un correo electrónico usando la cuenta de Gmail.
    """

    # Datos del servidor
    server = "smtp.gmail.com"
    port = 587

    # Crear la conexión al servidor de email.
    connection = smtplib.SMTP(host=server, port=port)
    connection.starttls()

    try:
        connection.login(user=credentials["username"],
                        password=credentials["password"])
    except:
        show_error("El usuario o la contraseña no són válidos.😡")
        return

    # Crear el mensaje.
    message = MIMEMultipart()
    message["To"] = email["to"]
    message["From"] = credentials["username"]
    message["Subject"] = email["subject"]
    message.attach(MIMEText(email["content"], "html"))

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


credentials = login()
new_mail = compose_email()

send_mail(credentials, new_mail)


# # programar tarea para enviar correo electrónico cada hora
# schedule.every().hour.do(send_mail)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
