from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from flask import abort
import logging

from core.extensions import db
from schemas.registration import RegistrationCreate
from models.registration import Registration

logger = logging.getLogger(__name__)

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

        logger.info("Registration created", extra={"registration_id": new_registration.id})
        return new_registration

    @staticmethod
    def get_all() -> list[Registration]:
        registrations = db.session.execute(select(Registration)).scalars().all()

        logger.info("Registration list shown")
        return [registration for registration in registrations]

    @staticmethod
    def get_registration_by_id(registration_id: int) -> Registration:
        registration = db.session.execute(select(Registration).where(Registration.id == registration_id)).scalar_one_or_none()

        if registration is None:
            abort(404, description=f"registration {registration_id} does not exist")

        logger.info("Registration created", extra={"registration_id": registration.id})
        return registration

    @staticmethod
    def delete_registration_by_id(registration_id: int) -> dict:
        registration = db.session.execute(select(Registration).where(Registration.id == registration_id)).scalar_one_or_none()

        if registration is None:
            abort(404, description=f"registration {registration_id} does not exist")

        db.session.delete(registration)
        db.session.commit()

        logger.info("Registration deleted", extra={"registration_id": registration.id})
        return {"message": "registration has been deleted", "data": registration.to_dict()}

    @staticmethod
    def update_registration(session_id: int, data: dict) -> Registration:
        registration = db.session.execute(
            select(Registration).where(Registration.id == session_id)
        ).scalar_one_or_none()

        if registration is None:
            return None

        registration_data = RegistrationCreate(**data)

        for key, value in registration_data.model_dump().items():
            setattr(registration, key, value)

        db.session.commit()

        logger.info("Registration updated", extra={"registration_id": registration.id})
        return registration