from fastapi import FastAPI
from .core.config import dbSetting

app = FastAPI()


@app.get("/")
def homepage():
    return {
        "message": f"Hi this is my first real project in python . And i am {dbSetting.POSTGRES_USER}"
    }
