from bs4 import BeautifulSoup
from mylib import *
import requests
import openai


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

    # Buscar las etiquetas <span> que tengan la clase "titleline" para obtener los
    # titulares.
    return soup.find_all(tag_to_find, class_to_find)


def get_openai_api_key():
    """
    Description: Devuelve una tupla con la API KEY y el OrganizationID
                 de Open Ai
    """

    with open("./094-openai_secrets.dat", mode="r", encoding="UTF-8") as file:
        api_key = file.readline().strip()
        organization_id = file.readline().strip()

    return {"api_key": api_key, "organization_id": organization_id}


def sumarize_me(text: str):
    """
    Description: Genera un resumen de un artículo dado a través de OpenIA
    Parameters:  - url: es el URL del artículo.
    """

    openai_secrets = get_openai_api_key()

    openai.organization = openai_secrets["organization_id"]
    openai.api_key = openai_secrets["api_key"]
    openai.Model.list()

    prompt = f"Summarize: {text} in 3 paragraphs"
    response = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=6)

    return response["choices"][0]["text"].strip()


def generate_text_to_sumarize(url: str):
    """
    Description: Genera el texto a partir de las etiquetas <p> del artículo
                 que se usará para realizar el resumen.
    """

    article = scraping_me(url, "div", {"class": "mw-parser-output"})
    # Usar el segundo resultado [1] porque el primero no trae nada en este caso.
    article = article[1]
    # Extraer sólo los párrafos.
    article = article.find_all("p")
    # Preparar el texto para resumir.
    article_text = ""
    for paragraph in article:
        article_text += paragraph.text

    return article_text


def get_references(url: str):
    references = scraping_me(url, "ol", {"class": "references"})[0]
    references = reference.find_all("li")
    result = ""
    for index, line in enumerate(references):
        # Reemplazar el caracter de inicio de la referencia "^ " con nada por
        # estética.
        line = line.text.replace("^ ", "")
        result += f"{index + 1} - {line}"

    return result


url = "https://en.wikipedia.org/wiki/Hair_loss"
article_content = generate_text_to_sumarize(url)
# sumary = sumarize_me()

clear_screen()
print(color_me("Resumen de Wikipedia", "yellow"))
# print(sumary, "\n")
print(color_me("Referencias:", "blue"))
reference = scraping_me(url, "ol", {"class": "references"})[0]
reference = reference.find_all("li")
print(get_references(url))