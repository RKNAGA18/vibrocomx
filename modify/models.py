from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    summary = db.Column(db.String(500))
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    # Extras from previous, keeping for compatibility
    author = db.Column(db.String(100), default="VibrocomX Team")
    tags = db.Column(db.String(200))
    image_url = db.Column(db.String(500))

class PageContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(50), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)

class SocialLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    icon_class = db.Column(db.String(100))

class Founder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100))
    bio = db.Column(db.Text)
    image_url = db.Column(db.String(500))

class SiteSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    setting_key = db.Column(db.String(100), unique=True, nullable=False)
    setting_value = db.Column(db.String(500))
