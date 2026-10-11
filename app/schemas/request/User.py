from pydantic import BaseModel, Field, EmailStr


class UserRegisterRequest(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=300,
    )


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=300,
    )
