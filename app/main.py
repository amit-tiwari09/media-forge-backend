from fastapi import FastAPI, Depends, APIRouter
from .core.config import dbSetting
from app.core.database import get_db
from app.models.User import User

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")


@app.get("/")
def homepage():
    return {
        "message": f"Hi this is my first real project in python . And i am {dbSetting.POSTGRES_USER}"
    }


@v1_router.post("/file")
def upload_convert_file():
    return {"message": "The Api Endpoint is working fine"}


app.include_router(v1_router)
