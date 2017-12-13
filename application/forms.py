from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email address', [DataRequired(), Email()]) #render_kw={"placeholder": "Email address"}
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField('remember me', default=False)


class PostFrom(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('Body')
