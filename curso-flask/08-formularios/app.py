from flask import Flask, render_template
import forms

app = Flask(__name__)


@app.route("/")
def index():
    comment_form = forms.CommentForm()
    title = "Curso de Flask - Formularios"
    return render_template("index.html", title=title, form=comment_form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
