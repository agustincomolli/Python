from mylib import color_me
import requests
import openai


def get_openai_api_key():
    """
    Description: Devuelve una tupla con la API KEY y el OrganizationID
                 de Open Ai
    """

    with open("./094-openai_secrets.dat", mode="r", encoding="UTF-8") as file:
        api_key = file.readline().strip()
        organization_id = file.readline().strip()

    return (api_key, organization_id)


def get_news_api_key():
    """
    Description: Lee el archivo con la API de news
    """

    with open("./094-news_secrets.dat", mode="r", encoding="UTF-8") as file:
        api_key = file.readline()

    return api_key.strip()


def get_news(country: str):
    """
    Description: Devuelve un JSON con las noticias del país elegido.
    """

    api_key = get_news_api_key()
    url = ('https://newsapi.org/v2/top-headlines?'
           f'country={country}&'
           f'apiKey={api_key}')

    response = requests.get(url)

    return response.json()


openai_secrets = {"api_key": "", "organization_id": ""}
openai_secrets["api_key"], openai_secrets["organization_id"] = get_openai_api_key()
articles = get_news("ar")["articles"]

openai.organization = openai_secrets["organization_id"]
openai.api_key = openai_secrets["api_key"]
openai.Model.list()

for article in articles:
    print(color_me(article["title"], "green"))
    prompt = f"Summarize: {article['url']}"
    response = openai.Completion.create(
            model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=6)
    print(response["choices"][0]["text"].strip(), "\n")
