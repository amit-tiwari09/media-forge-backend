from fastapi import Depends, Request, status, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.UserRepository import UserRepository
from app.services.AuthService import AuthService
from app.exceptions.AppException import AppException
from app.core.security import decodeAccessToken
import jwt


def getUserRepository(db: Session = Depends(get_db)):
    return UserRepository(db)


def getAuthService(userRepo: UserRepository = Depends(getUserRepository)):
    return AuthService(userRepo)


def auth_required(request: Request):

    authorization = request.headers.get("Authorization")

    if not authorization or not authorization.startswith("Bearer "):
        raise AppException(
            message="Authentication required",
            statusCode=status.HTTP_401_UNAUTHORIZED,
            errors=None,
        )

    token = authorization.split(" ", 1)[1]

    try:
        payload = decodeAccessToken(token)
        user_id = int(payload["sub"])

    except (jwt.InvalidTokenError, KeyError, TypeError, ValueError):

        raise AppException(
            message="invalid or expired token",
            statusCode=status.HTTP_401_UNAUTHORIZED,
            errors=None,
        )

    return user_id
