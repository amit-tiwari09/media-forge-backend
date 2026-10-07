from abc import ABC, abstractmethod
from app.models.User import User


class UserRepositoryInterface(ABC):

    @abstractmethod
    def add(self, User: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int, columns: list[str]) -> User | None:
        pass

    @abstractmethod
    def list_all(self, columns: list[str]) -> list[User]:
        pass
