from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from core.extensions import db
from schemas.registration import RegistrationCreate
from models.registration import Registration

class RegistrationService:
    @staticmethod
    def validate_registration(user_id: int) -> Registration | None:
        return db.session.execute(select(Registration).where(Registration.user_id == user_id)).scalar_one_or_none()

    @staticmethod
    def create_registration(data: RegistrationCreate) -> Registration | dict:
        is_registered = RegistrationService.validate_registration(data.user_id)
        if is_registered:
            return {"Error": f"User with id {data.user_id} already registered"}

        new_registration = Registration(
            user_id=data.user_id,
            conference_id=data.conference_id
        )
        try:
            db.session.add(new_registration)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            raise e
        except Exception as e:
            raise e

        return new_registration

    @staticmethod
    def get_all() -> list[Registration]:
        registrations = db.session.execute(select(Registration)).scalars().all()

        return [registration for registration in registrations]

    @staticmethod
    def get_registration_by_id(registration_id: int) -> Registration | None:
        registration = db.session.execute(select(Registration).where(Registration.id == registration_id)).scalar_one_or_none()

        return registration if registration else None

    @staticmethod
    def delete_registration_by_id(registration_id: int) -> dict | None:
        registration = db.session.execute(select(Registration).where(Registration.id == registration_id)).scalar_one_or_none()

        if registration:
            db.session.delete(registration)
            db.session.commit()
            return {"Message": "Registration has been deleted", "data": registration.to_dict()}
        else:
            return None
