from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField('remember me', default=False)


class RegisterForm(FlaskForm):
    nickname = StringField([DataRequired()], render_kw={"placeholder": "Nickname"})
    email = StringField([DataRequired()], render_kw={"placeholder": "Email"})
    password = PasswordField([DataRequired()], render_kw={"placeholder": "Password"})
    confirm = PasswordField('repeat password', [
        DataRequired(),
        EqualTo('password', message='passwords must match')], render_kw={"placeholder": "Repeat password"})


class PostFrom(FlaskForm):
    title = StringField('Title')
    body = TextAreaField('Body')
