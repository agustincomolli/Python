# En mi cuenta de Gmail, ir a Seguridad, en la sección Iniciar sesión con
# Googlez ir a Contraseñas de Aplicaciones y generar una par Gmail.
import smtplib
import schedule
import time
import requests
from bs4 import BeautifulSoup
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


def manage_events():
    """
    Description: Si hay eventos no enviados, crea el cuerpo del email con los
                 eventos y sus hipervínculos; y actualiza el diccionario de
                 eventos ya enviados.
    """

    new_events = get_events()
    events_to_send = {}
    content_email = ""
    # Recorrer los eventos obtenidos.
    for key, value in new_events.items():
        # Si no se ha enviado previamente...
        if not key in old_events:
            # Crear el cuerpo del mail con los eventos a enviar.
            events_to_send[key] = value
            print(key)
            content_email += f"<p><a href='{value}'>{key}</a></p>\n"
            # Actualizar el diccionario de eventos enviados.
            old_events[key] = value
    
    return content_email


def compose_mail(address:str):
    """
    Description: Crea el mensaje de email con todos los campos 
                 correspondientes.
    """
    content_email = manage_events()
    # Crear el mensaje.
    message = MIMEMultipart()
    message["To"] = address
    message["From"] = address
    message["Subject"] = "Nuevos eventos de la comunidad de Replit"
    message.attach(MIMEText(content_email, "html"))

    return message


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

    try:
        connection.login(user=credentials["username"],
                         password=credentials["password"])
    except:
        show_error("El usuario o la contraseña no són válidos.😡")
        return

    # Crear el mensaje.
    message = compose_mail(credentials["username"])

    try:
        # Enviar el mensaje.
        connection.send_message(message)
    except:
        show_error("El mensaje no se ha podido enviar 😭")
    else:
        print(color_me("\nMensaje enviado ✔️", "magenta"))
    finally:
        # Eliminar la variable message para no consumir más RAM.
        del message
        connection.quit()


def scraping_me(url: str, tag_to_find: str, class_to_find: dict):
    """
    Description: Devuelve un objeto con los resultados de la búsqueda.
    Parameters:  - url: URL del sitio a escanear.
                 - tag_to_find: etiqueta HTML que se va a buscar.
                 - class_to_find: diccionario que contiene la clase css
                                  de la etiqueta a buscar.
    """

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    return soup.find_all(tag_to_find, class_to_find)


def get_event_name(link):
    """
    Description: Devuelve un string que contiene el nombre del evento,
                 seguido de su fecha.
    """

    # Buscar las etiquetas que contienen el nombre del evento y la fecha.
    spans = link.find_all("span")
    event_name = spans[0].text
    event_date = spans[1].text

    return f"{event_name}, {event_date}"


def get_events():
    """
    Description: Busca los eventos dentro de la página que coincidan con los
                 filtros de búsqueda.
    """

    url = "https://replit.com/community-hub"
    result_search = scraping_me(url, "ul", {"class": "css-fod6u7"})
    filter_list = ["Python", "Replit", "Helpline", "Code"]
    events_dict = {}

    # Trabajar SOLO con el primer resultado de la búsqueda...
    # Buscar los hipervínculos.
    links = result_search[0].find_all("a")
    for link in links:
        event_title = get_event_name(link)
        for word in event_title.split():
            # Si el evento coincide con el filtro...
            if word in filter_list:
                events_dict[event_title] = link["href"]
                break

    return events_dict


old_events = {} # Guarda los eventos que han sido enviados por correo.

# Programar tarea para enviar correo electrónico cada hora
schedule.every(6).hours.do(send_mail)

while True:
    schedule.run_pending()
    # Esperar una hora.
    time.sleep(3600)
