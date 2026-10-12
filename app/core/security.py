from pwdlib import PasswordHash

from datetime import datetime, timezone, timedelta
from app.core.config import dbSetting
import jwt

passwordHash = PasswordHash.recommended()


def hashPassword(password: str) -> str:
    return passwordHash.hash(password)


def verifyPassword(password: str, hashedPassword: str) -> bool:
    return passwordHash.verify(password, hashedPassword)


def createAccessToken(userId: int, userUuid: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=dbSetting.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(userId),
        "uuid": str(userUuid),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        dbSetting.JWT_SECRET_KEY,
        algorithm=dbSetting.JWT_ALGORITHM,
    )


def decodeAccessToken(accessToken: str) -> dict:
    return jwt.decode(
        accessToken,
        dbSetting.JWT_SECRET_KEY,
        algorithms=[dbSetting.JWT_ALGORITHM],
    )
