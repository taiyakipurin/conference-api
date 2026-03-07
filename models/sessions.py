from database import db
from datetime import datetime

class Session(db.Model):
    __tablename__ = 'sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id')
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    speaker = db.Column(db.String(50))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)