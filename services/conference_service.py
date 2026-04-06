from core.extensions import db
from sqlalchemy import select
from pydantic import ValidationError
from flask import abort
import logging

from models.conference import Conference
from schemas.conference import ConferenceCreate

logger = logging.getLogger(__name__)

class ConferenceService:

    @staticmethod
    def create_conference(data: dict) -> Conference:
        conf_data = ConferenceCreate(**data)

        conference = Conference(**conf_data.model_dump())

        db.session.add(conference)
        db.session.commit()

        logger.info("Conference created", extra={"conference_id": conference.id})
        return conference
        
    @staticmethod
    def get_all() -> list[Conference]:
        conferences = db.session.execute(select(Conference)).scalars().all()

        logger.info("Conference list shown")
        return [conference.to_dict() for conference in conferences]

    @staticmethod
    def get_conference_by_id(conference_id: int) -> Conference:
        conference = db.session.execute(select(Conference).where(Conference.id == conference_id)).scalar_one_or_none()

        if conference is None:
            abort(404, description=f"conference {conference_id} does not exist")

        logger.info("Conference shown", extra={"conference_id": conference.id})
        return conference

    @staticmethod
    def delete_conference_by_id(conference_id: int) -> dict:
        conference = db.session.execute(select(Conference).where(Conference.id == conference_id)).scalar_one_or_none()

        if conference is None:
            abort(404, description=f"conference {conference_id} does not exist")

        db.session.delete(conference)
        db.session.commit()

        logger.info("Conference deleted", extra={"conference_id": conference.id})
        return {"message": f"conference {conference_id} has been deleted", "data": conference.to_dict()}

    @staticmethod
    def update_conference(conference_id: int, data: dict) -> Conference:
        conference = db.session.execute(
            select(Conference).where(Conference.id == conference_id)
        ).scalar_one_or_none()

        if conference is None:
            return None

        conf_data = ConferenceCreate(**data)

        for key, value in conf_data.model_dump().items():
            setattr(conference, key, value)

        db.session.commit()

        logger.info("Conference updated", extra={"conference_id": conference.id})
        return conference