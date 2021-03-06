from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import check_password_hash

from models import User


class LoginForm(FlaskForm):
    email = StringField('Email address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])
    remember_me = BooleanField('remember me', default=False)

    def validate(self):
        check_validate = super(LoginForm, self).validate()
        if not check_validate:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            self.email.errors.append('Invalid email or password')
            return False

        if not check_password_hash(user.password, self.password.data):
            self.email.errors.append('Invalid email or password')
            return False
        return True


class RegisterForm(FlaskForm):
    nickname = StringField([DataRequired()], render_kw={"placeholder": "Nickname", 'autofocus': True})
    email = StringField([DataRequired()], render_kw={"placeholder": "Email"})
    password = PasswordField([DataRequired()], render_kw={"placeholder": "Password"})
    confirm = PasswordField('repeat password', [
        DataRequired(),
        EqualTo('password', message='passwords must match')], render_kw={"placeholder": "Repeat password"})

    def validate(self):
        check_validate = super(RegisterForm, self).validate()
        if not check_validate:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('User with that email already exists')
            return False
        return True


class PostFrom(FlaskForm):
    title = StringField('Title', [DataRequired()])
    body = TextAreaField('Body', [DataRequired()])

    def validate(self):
        return super(PostFrom, self).validate()
