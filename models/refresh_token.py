from core.extensions import db
from datetime import datetime

class RefreshToken(db.Model):
    __tablename__ = 'refresh_tokens'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='refresh_token')
    token_hash = db.Column(db.String(255), nullable=False) 
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    expires_at = db.Column(db.DateTime, nullable=False)
    