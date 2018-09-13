from datetime import datetime
from flask import render_template, request, redirect, url_for, g, flash
from flask_login import login_user, logout_user, current_user, login_required

from forms import PostFrom, LoginForm, RegisterForm
from models import Post, User
from application import app, db, login_manager


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route("/create_post", methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostFrom(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("main"))
    return render_template("create_post.html", title="Create post", form=form)

# @app.route("edit_post", methods=['GET', 'POST'])
# @login_required
# def edit_post():
#     form =
#     if request.method == 'POST' and form.validate_on_submit():
#         pass
#         return redirect(url_for())
#     return render_template()
#
# @app.route("delete_post", methods=['GET', 'POST'])
# def delete_post():
#     form =
#     if request.method == 'POST' and form.validate_on_submit():
#         pass
#         return redirect(url_for())
#     return render_template()


@app.route("/", methods=['GET', 'POST'])
@login_required
def main():
    posts = Post.query.order_by(Post.title) #.paginate(1, 2, False).items
    return render_template("index.html", title='Home', posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main'))
    return render_template("login.html", title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.nickname.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/user/<nickname>", methods=['GET', 'POST'])
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first_or_404()
    if user:
        return render_template('user.html', title='Profile', user=user)
    return redirect(url_for('main'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
