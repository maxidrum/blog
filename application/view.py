from flask import render_template, request, redirect, url_for

from forms import PostFrom
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
