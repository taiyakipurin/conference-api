from core.extensions import db
from sqlalchemy import select

from models.conference import Conference
from schemas.conference import ConferenceCreate

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
    def get_all() -> list[Conference]:
        conferences = db.session.execute(select(Conference)).scalars().all()

        return [conference.to_dict() for conference in conferences]

    @staticmethod
    def get_conference_by_id(conference_id: int) -> Conference | None:
        conference = db.session.execute(select(Conference).where(Conference.id == conference_id)).scalar_one_or_none()

        return conference if conference else None

    @staticmethod
    def delete_conference_by_id(conference_id: int) -> dict | None:
        conference = db.session.execute(select(Conference).where(Conference.id == conference_id)).scalar_one_or_none()

        if conference:
            db.session.delete(conference)
            db.session.commit()
            return {"message": "conference has been deleted", "data": conference.to_dict()}
        else:
            return None