from database import db

from models.session import Session
from schemas.session import SessionCreate

class SessionService:
    @staticmethod
    def create_session(data: SessionCreate):
        new_session = Session(
            # conference_id=data.conference_id,
            title=data.title,
            description=data.description,
            speaker=data.speaker,
            start_time=data.start_time,
            end_time=data.end_time
        )
        
        try:
            db.session.add(new_session)
            db.session.commit()
        except Exception as e:
            raise Exception(e)

        # return {"data": new_session.to_dict()}
        return {"message": "new session has been added", "data": new_session.to_dict()}
        
