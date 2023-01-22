from .models import *
from sqlalchemy.orm import Session
from .validation import UserValidation
from run import route


def home():
    return {"msg": "Welcome to FastAPI portal"}


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserValidation):
    db_user = User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        is_active=user.is_active
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
