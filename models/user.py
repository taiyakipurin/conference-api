from core.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    refresh_token = db.relationship('RefreshToken', back_populates='user') 
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    password_hash = db.Column(db.String(255), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name, 
            "email": self.email,
            "phone": self.phone,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
    