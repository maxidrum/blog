from flask import render_template

from application import app

@app.route("/")
def main():
    return render_template("base.html")
