from wtforms import Form, StringField, TextAreaField, EmailField


class CommentForm(Form):
    user_name = StringField("Usuario:")
    email = EmailField("Correo electrónico:")
    comment = TextAreaField("Comentario:")
