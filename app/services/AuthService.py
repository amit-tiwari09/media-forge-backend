from fastapi import HTTPException
from app.repositories import UserRepository
from app.schemas.request.User import UserRegisterRequest, UserLoginRequest
from app.models.User import User
from app.core.security import hashPassword

from app.exceptions.AppException import AppException


class AuthService:
    def __init__(self, userRepo: UserRepository):
        self.userRepo = userRepo

    # ======= Register new User
    def register(self, data: UserRegisterRequest):

        if self.userRepo.isEmailExists(data.email):
            raise AppException(
                message="Email already exists",
                statusCode=409,
                errors={"email": ["This email is already registered."]},
            )

        return self.userRepo.add(
            User(name=data.name, email=data.email, password=hashPassword(data.password))
        )

    # ======= Login User
    def login(self, data: UserLoginRequest):

        user = self.userRepo.get_by_credentials(data.email)

        if not user:
            raise AppException(message="Wrong Credentials", statusCode=401)
