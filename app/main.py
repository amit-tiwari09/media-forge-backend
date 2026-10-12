from fastapi import FastAPI, Depends, APIRouter, status
from .core.config import dbSetting
from app.core.database import get_db
from app.models.User import User
from app.schemas.request.User import UserRegisterRequest, UserLoginRequest
from app.services.AuthService import AuthService
from app.core.dependency import getAuthService


from app.exceptions.AppException import AppException
from fastapi.exceptions import RequestValidationError
from app.handler.ExceptionHandler import (
    appExceptionHandler,
    validationExceptionHandler,
    unexpectedExceptionHandler,
)

from app.core.response import successResponse
from app.schemas.response.UserResponse import UserResponse

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")


# ======= Auth Routes =======
# ==register
@v1_router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
def register(
    userData: UserRegisterRequest, authService: AuthService = Depends(getAuthService)
):
    response = authService.register(userData)

    return successResponse(
        message="User registered successfully",
        data=response,
    )


# ==login
@v1_router.post("/login", status_code=status.HTTP_201_CREATED)
def login(data: UserLoginRequest, authService: AuthService = Depends(getAuthService)):
    response = authService.login(data)

    return successResponse(message="User Authentication Success", data=response)


@app.get("/")
def homepage():
    return {
        "message": f"Hi this is my first real project in python . And i am {dbSetting.POSTGRES_USER}"
    }


@v1_router.post("/file")
def upload_convert_file():
    return {"message": "The Api Endpoint is working fine"}


app.include_router(v1_router)


# ======Exception Handlers

app.add_exception_handler(
    AppException,
    appExceptionHandler,
)

app.add_exception_handler(
    RequestValidationError,
    validationExceptionHandler,
)

app.add_exception_handler(
    Exception,
    unexpectedExceptionHandler,
)
