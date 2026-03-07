from database import db
from models.conference import Conference
from schemas.conference_schema import ConferenceCreate

class ConferenceService:
    @staticmethod
    def create_conference(data: ConferenceCreate):
        # conference = Conference(**data)
        
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
        except ValidationError as e:
            return {"error": e}
        except Exception as e:
            raise Exception(e)
        
        # return new_conference
        return 0
        
    @staticmethod
    def get_conferences():
        return Conference.query.all()