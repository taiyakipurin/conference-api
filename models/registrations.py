from database import db
from datetime import datetime

class Registration(db.Model):
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)