from core.extensions import db
from sqlalchemy import select
from flask import abort
import logging

from models.user import User
from schemas.user import UserRegisterSchema

logger = logging.getLogger(__name__)

class UserService:
    @staticmethod
    def get_all_users() -> list[User]:
        users = db.session.execute(select(User)).scalars().all()

        logger.info("User list shown")
        return [user.to_dict() for user in users]

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        user = db.session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

        if user is None:
            abort(404, description="user does not exist")

        logger.info("User shown", extra={"user_id": user.id})
        return user

    @staticmethod
    def delete_user_by_id(user_id: int) -> dict:
        user = db.session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

        if user is None:
            abort(404, "user does not exist")

        db.session.delete(user)
        db.session.commit()

        logger.info("User deleted", extra={"user_id": user.id})
        return {"message": "user has been deleted", "data": user.to_dict()}

    @staticmethod
    def update_user(user_id: int, data: dict) -> User:
        user = db.session.execute(
            select(User).where(User.id == user_id)
        ).scalar_one_or_none()

        if user is None:
            return None

        user_data = UserRegisterSchema(**data)

        for key, value in user_data.model_dump().items():
            setattr(user, key, value)

        db.session.commit()

        logger.info("User updated", extra={"user_id": user.id})
        return user