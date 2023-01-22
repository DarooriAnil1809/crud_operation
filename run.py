from fastapi import FastAPI
from sqlalchemy.orm import Session
from configuration.database import SessionLocal, engine
from app.views import *
from app.validation import *
from fastapi import Depends, FastAPI, HTTPException


route = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@route.post("/users/", response_model=UserValidation)
def create_user(user: UserValidation, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
