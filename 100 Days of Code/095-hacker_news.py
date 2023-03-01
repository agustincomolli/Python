from bs4 import BeautifulSoup
import requests


url = "https://news.ycombinator.com/news"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# Buscar las etiquetas <span> que tengan la clase "titleline" para obtener los
# titulares.
result_search = soup.find_all("span", {"class" : "titleline"})
filter_list = ["Python", "Replit", "Microsoft", "Google"]

# Recorrer los titulares, dividirlos en palabras y ver si alguna coincide con
# el filtro para mostrarlo.
for index, result in enumerate(result_search):

    for word in result.text.split():

        if word in filter_list:
            print(f"{index + 1} - {result.text}")
            # Buscar los links del resultado para mostrarlo.
            link = result.find_all("a")
            print(f"     Link: {link[0]['href']}")
