from sqlalchemy.orm import Session
from app.repositories.interfaces import UserRepositoryInterface
from app.models.User import User


class UserRepository(UserRepositoryInterface):
    def __int__(self, session: Session):
        self.session = session

    def add(self, User: User) -> User:
        self.session.add(User)
        self.session.commit()
        self.session.refresh(User)

        return User

    def get_by_id(self, user_id: int, columns: list[str]) -> User | None:
        pass

    def list_all(self, columns: list[str]) -> list[User]:
        pass
