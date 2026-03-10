from database import db

from models.conference_model import Conference
from schemas.conference_schema import ConferenceCreate

class ConferenceService:
    @staticmethod
    def create_conference(data: ConferenceCreate):
        new_conference = Conference(
            title=data.title,
            description=data.description,
            location=data.location,
            start_date=data.start_date,
            end_date=data.end_date
        )
        
        try:
            db.session.add(new_conference)
            db.session.commit()
        except Exception as e:
            raise Exception(e)
        
        return {"message": "conference has been created", "data": new_conference.to_dict()}
        
    @staticmethod
    def get_conferences():
        return Conference.query.all()