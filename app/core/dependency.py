from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.UserRepository import UserRepository
from app.services.AuthService import AuthService


def getUserRepository(db: Session = Depends(get_db)):
    return UserRepository(db)


def getAuthService(userRepo: UserRepository = Depends(getUserRepository)):
    return AuthService(userRepo)
