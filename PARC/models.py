from PARC import db
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ## nullable=False oblige le contenu
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    image_file = db.Column(db.String(20), nullable=False, default='logo.png')
    content = db.Column(db.Text, nullable=False)
    # relation avec author. Chaque post a un author

    def __repr__(self):
        return f"Post('{self.title}','{self.image_file}', '{self.date_posted}')"
