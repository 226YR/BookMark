import uuid
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    impression = db.Column(db.Text, nullable=False)
    favorite_flag = db.Column(db.Boolean, default=False)
    reading_time_minutes = db.Column(db.Integer, default=0)
    reading_status = db.Column(db.String(50), nullable=False, default='未読')
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())