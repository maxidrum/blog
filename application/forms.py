from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email address', [DataRequired(), Email()])  # render_kw={"placeholder": "Email address"}
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField('remember me', default=False)


class RegisterForm(FlaskForm):
    nickname = StringField('nickname', [DataRequired()])
    email = StringField('email', [DataRequired()])
    password = PasswordField('password', [DataRequired()])
    confirm = PasswordField('repeat password', [
        DataRequired(),
        EqualTo('password', message='passwords must match')
    ])


class PostFrom(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('Body')
