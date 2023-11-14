from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "title": "Plantillas",
        "h1": "Plantillas con archivos estáticos."
    }
    return render_template("index.html", data=data)

if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)