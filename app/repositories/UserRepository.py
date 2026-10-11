from sqlalchemy import select, exists
from sqlalchemy.orm import Session
from app.repositories.interfaces.UserRepositoryInterface import UserRepositoryInterface
from app.models.User import User


class UserRepository(UserRepositoryInterface):
    def __init__(self, session: Session):
        self.session = session

    def _columns(self, columns: list[str] | None):
        if columns is None:
            return [User]

        return [getattr(User, column) for column in columns]

    # Add specf record in the users table
    def add(self, User: User) -> User:
        self.session.add(User)
        self.session.commit()
        self.session.refresh(User)

        return User

    # return a user record mathing with id
    def get_by_id(self, user_id: int, columns: list[str] | None) -> User | None:
        return self.session.execute(
            select(*self._columns(columns)).where(User.id == user_id)
        ).scalar_one_or_none()

    # return a user record mathing with credentials like (email, phone etc)
    def get_by_credentials(
        self, credential: str, columns: list[str] | None
    ) -> User | None:
        return self.session.execute(
            select(*self._columns(columns)).where(User.email == credential)
        ).scalar_one_or_none()

    # list all the user records
    def list_all(self, columns: list[str] | None) -> list[User]:
        return self.session.execute(select(*self._columns(columns))).scalars().all()

    # check if the email exists already in db or not
    def isEmailExists(self, email: str) -> bool:
        return self.session.execute(
            select(exists().where(User.email == email))
        ).scalar()
