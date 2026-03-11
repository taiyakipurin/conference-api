from core.extensions import db
from sqlalchemy import select

from models.user import User


class UserService:
    @staticmethod
    def get_all_users() -> list[User]:
        users = db.session.execute(select(User)).scalars().all()

        return [user.to_dict() for user in users]

    @staticmethod
    def get_user_by_id(user_id: int) -> User | None:
        user = db.session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

        return user if user else None

    @staticmethod
    def delete_user_by_id(user_id: int) -> dict | None:
        user = db.session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

        if user:
            db.session.delete(user)
            db.session.commit()
            return {"Message": "User has been deleted", "data": user.to_dict()}
        else:
            return None
