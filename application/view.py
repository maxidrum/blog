from flask import render_template, request, redirect, url_for

from forms import PostFrom, LoginForm
from models import Post
from application import app, db

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
def main():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        # user = User.query.filter_by(username=form.data['email']).first()
    return render_template("login.html", form=form)
