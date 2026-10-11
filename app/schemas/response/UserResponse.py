from pydantic import BaseModel, ConfigDict
from uuid import UUID


class UserResponse(BaseModel):
    id: int
    uuid: UUID
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)
