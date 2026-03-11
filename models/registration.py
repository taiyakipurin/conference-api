from core.extensions import db
from datetime import datetime

from models.user import User

class Registration(db.Model):
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', foreign_keys=[user_id])

    def to_dict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'conference_id': self.conference_id,
            'created_at': self.created_at.isoformat(),
            'user': self.user.name if self.user else None
        }
