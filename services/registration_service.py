from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from flask import abort

from core.extensions import db
from schemas.registration import RegistrationCreate
from models.registration import Registration

class RegistrationService:
    @staticmethod
    def create_registration(data: RegistrationCreate) -> Registration:
        registration = db.session.execute(select(Registration).where(Registration.user_id == data.user_id)).scalar_one_or_none()

        if registration:
            abort(409, description=f"registration for user {data.user_id} already exists")

        new_registration = Registration(
            user_id=data.user_id,
            conference_id=data.conference_id
        )

        try:
            db.session.add(new_registration)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            abort(400, description="invalid id")

        return new_registration

    @staticmethod
    def get_all() -> list[Registration]:
        registrations = db.session.execute(select(Registration)).scalars().all()

        return [registration for registration in registrations]

    @staticmethod
    def get_registration_by_id(registration_id: int) -> Registration:
        registration = db.session.execute(select(Registration).where(Registration.id == registration_id)).scalar_one_or_none()

        if registration is None:
            abort(404, description=f"registration {registration_id} does not exist")

        return registration

    @staticmethod
    def delete_registration_by_id(registration_id: int) -> dict:
        registration = db.session.execute(select(Registration).where(Registration.id == registration_id)).scalar_one_or_none()

        if registration is None:
            abort(404, description=f"registration {registration_id} does not exist")

        db.session.delete(registration)
        db.session.commit()

        return {"message": "registration has been deleted", "data": registration.to_dict()}

