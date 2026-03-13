from core.extensions import db
from sqlalchemy import select
from flask import abort

from models.user import User


class UserService:
    @staticmethod
    def get_all_users() -> list[User]:
        users = db.session.execute(select(User)).scalars().all()

        return [user.to_dict() for user in users]

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        user = db.session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

        if user is None:
            abort(404, description="user does not exist")

        return user

    @staticmethod
    def delete_user_by_id(user_id: int) -> dict:
        user = db.session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

        if user is None:
            abort(404, "user does not exist")

        db.session.delete(user)
        db.session.commit()

        return {"message": "user has been deleted", "data": user.to_dict()}