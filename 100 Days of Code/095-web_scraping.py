from bs4 import BeautifulSoup
from mylib import *
import requests


url = "https://www.yelp.com/search?find_desc=&l="
url += "a%3A-35.0575957%2C-58.7690992%2C10830.436061807402"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

result_search = soup.find_all("a", {"class" : "css-1m051bw"})

for index, result in enumerate(result_search):
    print(f"{index + 1} - {result.text}")
    print(f"     https://www.yelp.com/{result['href']}")