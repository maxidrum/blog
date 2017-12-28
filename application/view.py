from flask import render_template, request, redirect, url_for,g
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required

from forms import PostFrom, LoginForm, RegisterForm
from models import Post, User
from application import app, db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user


@app.route("/create", methods=['GET', 'POST'])
def create_post():
    form = PostFrom()
    if request.method == 'POST':
        post = Post(title=form.data['title'], body=form.data['body']) #TODO: ref
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("main"))
    return render_template("create_post.html", form=form)


@app.route("/")
@login_required
def main():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
        return redirect(url_for('main'))
    return render_template("login.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.nickname.data, form.email.data, generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))