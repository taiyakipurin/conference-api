from core.extensions import db
from datetime import datetime

from models.user import User

class Registration(db.Model):
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True)

    user = db.relationship('User', foreign_keys=[User.id])
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    conference_id = db.Column(db.Integer, db.ForeignKey('conference.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)