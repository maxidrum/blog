from flask import render_template

from forms import PostFrom
from models import Post
from application import app

@app.route("/create")
def create_post():
    form = PostFrom()
    return render_template("create_post.html", form=form)


@app.route("/")
def main():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)
