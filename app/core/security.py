from pwdlib import PasswordHash

passwordHash = PasswordHash.recommended()


def hashPassword(password: str) -> str:
    return passwordHash.hash(password)