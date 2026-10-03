from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import dbSetting

DATABASE_URL = f"postgresql://{dbSetting.POSTGRES_USER}:{dbSetting.POSTGRES_PASSWORD}@{dbSetting.POSTGRES_HOST}:{dbSetting.POSTGRES_PORT}/{dbSetting.POSTGRES_DB}"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to open/close DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()
