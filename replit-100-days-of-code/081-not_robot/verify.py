from flask import Flask, request


def is_valid(data: dict):

    if data["question-1"] != "no":
        return False
    if data["question-2"] == "ED-209":
        return False
    if data["question-3"].lower() != "cinco":
        return False
    
    return True


app = Flask(__name__, static_url_path="/static")


@app.route("/verify", methods=["POST"])
def verify():
    form = request.form

    with open("./templates/template.html", mode="r", encoding="UTF-8") as file:
        page = file.read()

    if is_valid(form):
        message = f"<h2 class='message'>¡Bienvenido humano!</h2>"
        message += "<p class='icon'>🧑</p>"
    else:
        message = f"<h2 class='message'>¡Eres un estúpido robot!</h2>"
        message += "<p class='icon'>🤖</p>"

    page = page.replace("{content}", message)

    return page


@app.route("/")
def index():
    with open("./static/verify.html", mode="r", encoding="UTF-8") as file:
        page = file.read()
    return page


app.run(host="0.0.0.0", port=81)
