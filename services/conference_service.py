from core.extensions import db
from sqlalchemy import select
from pydantic import ValidationError
from flask import abort

from models.conference import Conference
from schemas.conference import ConferenceCreate

class ConferenceService:
    @staticmethod
    def create_conference(data: dict) -> Conference:
        conf_data = ConferenceCreate(**data)

        conference = Conference(**conf_data.model_dump())

        db.session.add(conference)
        db.session.commit()
        
        return conference
        
    @staticmethod
    def get_all() -> list[Conference]:
        conferences = db.session.execute(select(Conference)).scalars().all()

        return [conference.to_dict() for conference in conferences]

    @staticmethod
    def get_conference_by_id(conference_id: int) -> Conference:
        conference = db.session.execute(select(Conference).where(Conference.id == conference_id)).scalar_one_or_none()

        if conference is None:
            abort(404, description=f"conference {conference_id} does not exist")

        return conference

    @staticmethod
    def delete_conference_by_id(conference_id: int) -> dict:
        conference = db.session.execute(select(Conference).where(Conference.id == conference_id)).scalar_one_or_none()

        if conference is None:
            abort(404, description=f"conference {conference_id} does not exist")

        db.session.delete(conference)
        db.session.commit()

        return {"message": f"conference {conference_id} has been deleted", "data": conference.to_dict()}
