from core.extensions import db
from sqlalchemy import select
from flask import abort
import logging

from models.session import Session
from schemas.session import SessionCreate

logger = logging.getLogger(__name__)

class SessionService:
    @staticmethod
    def create_session(data: dict) -> dict:
        session_data = SessionCreate(**data)
        session = Session(**session_data.model_dump())

        db.session.add(session)
        db.session.commit()

        logger.info("Session created", extra={"session_id": session.id})
        return {"message": "new session has been added", "data": session.to_dict()}

    @staticmethod
    def get_all() -> list[Session]:
        sessions = db.session.execute(select(Session)).scalars().all()

        logger.info("Session list shown")
        return [session.to_dict() for session in sessions]

    @staticmethod
    def get_session_by_id(session_id: int) -> Session:
        session = db.session.execute(select(Session).where(Session.id == session_id)).scalar_one_or_none()

        if session is None:
            abort(404, description="session does not exist")

        logger.info("Session shown", extra={"session_id": session.id})
        return session

    @staticmethod
    def delete_session_by_id(session_id: int) -> dict:
        session = db.session.execute(select(Session).where(Session.id == session_id)).scalar_one_or_none()

        if session is None:
            abort(404, description="session does not exist")

        db.session.delete(session)
        db.session.commit()

        logger.info("Session deleted", extra={"session_id": session.id})
        return {"Message": "Session has been deleted", "data": session.to_dict()}

    @staticmethod
    def update_session(session_id: int, data: dict) -> Session:
        session = db.session.execute(
            select(Session).where(Session.id == session_id)
        ).scalar_one_or_none()

        if session is None:
            return None

        session_data = SessionCreate(**data)

        for key, value in session_data.model_dump().items():
            setattr(session, key, value)

        db.session.commit()

        logger.info("Session updated", extra={"session_id": session.id})
        return session
