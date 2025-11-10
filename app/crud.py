from __future__ import annotations
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from .models import User
from .security import hash_password
from . import schemas

def create_user(db: Session, user_in: schemas.UserCreate) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
        password_hash=hash_password(user_in.password),
    )
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists.",
        )
    return user

def get_user(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)

def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()