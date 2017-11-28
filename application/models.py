from application import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
