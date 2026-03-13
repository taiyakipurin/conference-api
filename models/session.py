from core.extensions import db

class Session(db.Model):
    __tablename__ = 'sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    speaker = db.Column(db.String(50))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            "id": self.id,
            "conference_id": self.conference_id,
            "title": self.title,
            "description": self.description,
            "speaker": self.speaker,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None
        }