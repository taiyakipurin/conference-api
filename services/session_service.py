from core.extensions import db
from sqlalchemy import select

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

        return {"message": "new session has been added", "data": new_session.to_dict()}

    @staticmethod
    def get_all() -> list[Session]:
        sessions = db.session.execute(select(Session)).scalars().all()

        return [session.to_dict() for session in sessions]

    @staticmethod
    def get_session_by_id(session_id: int) -> Session | None:
        session = db.session.execute(select(Session).where(Session.id == session_id)).scalar_one_or_none()

        return session if session else None

    @staticmethod
    def delete_session_by_id(session_id: int) -> dict | None:
        session = db.session.execute(select(Session).where(Session.id == session_id)).scalar_one_or_none()

        if session:
            db.session.delete(session)
            db.session.commit()
            return {"Message": "Session has been deleted", "data": session.to_dict()}
        else:
            return None
