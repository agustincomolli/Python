from flask import Flask

reflections = {}

reflections["76"] = {
    "link": "https://replit.com/@agustin-comolli/Dia-76-de-100",
    "reflection": "Una introducción a Flask"
}

reflections["77"] = {
    "link": "https://replit.com/@agustin-comolli/Dia-77-de-100",
    "reflection": "Una aplicación de blogs"
}

app = Flask(__name__, static_url_path="/static")


@app.route("/<page_number>")
def index(page_number):
    with open("./template/template.html", mode="r", encoding="UTF-8") as file:
        page = file.read()

    page = page.replace("{number_day}", page_number)
    page = page.replace("{link}", reflections[page_number]["link"])
    page = page.replace("{reflection}", reflections[page_number]["reflection"])

    return page


app.run(host="0.0.0.0", port=81)
